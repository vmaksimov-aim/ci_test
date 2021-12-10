import datetime
import uuid
from typing import Awaitable, List, Optional, Type

from tornado import iostream
from tornado.concurrent import future_set_result_unless_cancelled
from tornado.web import HTTPError, OutputTransform, RequestHandler
from tornado_sqlalchemy import SessionMixin

from powerloop.common.constants import ContentType, HttpHeaders, HttpStatus
from powerloop.common.exceptions import ApplicationException, RequestValidationException
from powerloop.configuration import logger
from powerloop.configuration.context import LocalContext
from powerloop.configuration.validator import create_validator
from powerloop.utils.session import make_session


class BaseRequestHandler(SessionMixin, RequestHandler):
    validator = create_validator()

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        """
        Implement this method to handle streamed request data.
        Requires the `.stream_request_body` decorator.
        May be a coroutine for flow control.
        """

    def write_response(self, response):
        self.write(response)

    def prepare(self):
        self._create_request_id()
        http_method = self.request.method.lower()
        method_name = f'prepare_{http_method}_request'

        if hasattr(self, method_name):
            method = getattr(self, method_name)
            method()

    def options(self, *args, **kwargs):
        self.set_status(HttpStatus.NO_CONTENT)
        self.finish()

    def set_default_headers(self):
        self.set_header(HttpHeaders.ACCESS_CONTROL_ALLOW_ORIGIN, '*')
        self.set_header(HttpHeaders.ACCESS_CONTROL_ALLOW_HEADERS, '*')
        self.set_header(HttpHeaders.ACCESS_CONTROL_ALLOW_METHODS, 'POST, GET, DELETE, PUT, PATCH, OPTIONS')

    def write_error(self, status_code, **kwargs):
        self.set_header(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON)

        response = _create_json_error(self._reason, status_code, kwargs.get('exc_info'))

        self.finish(response)

    def request_summary(self) -> str:
        method = self.request.method
        uri = self.request.uri
        remote_ip = self.request.remote_ip

        return f'method: [{method}] url: [{uri}] remote_ip: [{remote_ip}]'

    def _validate_request(self, validation_object, validation_schema):
        if not self.validator.validate(validation_object, validation_schema):
            raise RequestValidationException(str(self.validator.errors))

    def _create_request_id(self):
        self.request_id = str(uuid.uuid4())
        LocalContext.request_id.set(self.request_id)

    async def _execute(self, transforms: List['OutputTransform'], *args: bytes, **kwargs: bytes) -> None:
        """Executes this request with the given output transforms."""
        self._transforms = transforms
        try:
            if self.request.method not in self.SUPPORTED_METHODS:
                raise HTTPError(HttpStatus.METHOD_NOT_ALLOWED)
            self.path_args = [self.decode_argument(arg) for arg in args]
            self.path_kwargs = {
                kwargs_key: self.decode_argument(kwargs_value, name=kwargs_key)
                for kwargs_key, kwargs_value in kwargs.items()
            }
            # If XSRF cookies are turned on, reject form submissions without
            # the proper cookie
            if self.request.method not in {'GET', 'HEAD', 'OPTIONS'} and self.application.settings.get('xsrf_cookies'):
                self.check_xsrf_cookie()

            result = self.prepare()
            if result is not None:
                result = await result
            if self._prepared_future is not None:
                # Tell the Application we've finished with prepare()
                # and are ready for the body to arrive.
                future_set_result_unless_cancelled(self._prepared_future, None)
            if self._finished:
                return

            if self._has_stream_request_body(self.__class__):
                # In streaming mode request.body is a Future that signals
                # the body has been completely received.  The Future has no
                # result; the data has been passed to self.data_received
                # instead.
                try:
                    await self.request.body_future
                except iostream.StreamClosedError:
                    return

            method = getattr(self, self.request.method.lower())

            with make_session() as request_session:
                LocalContext.session.set(request_session)
                result = method(*self.path_args, **self.path_kwargs)

                if result is not None:
                    result = await result

            if result:
                self.write_response(result)

            if self._auto_finish and not self._finished:
                await super().finish()
        except Exception as e:
            try:
                self._handle_request_exception(e)
            except Exception as error:
                logger.error(f'Exception in exception handler [{error}]', exc_info=True)
            finally:
                # Unset result to avoid circular references
                result = None
            if self._prepared_future is not None and not self._prepared_future.done():
                # in a finally block to avoid GC issues prior to Python 3.4.
                self._prepared_future.set_result(None)

    @staticmethod
    def _has_stream_request_body(cls: Type[RequestHandler]) -> bool:
        if not issubclass(cls, RequestHandler):
            raise TypeError(f'expected subclass of RequestHandler, got {cls}')

        return cls._stream_request_body


def _create_json_error(reason, status_code, exception_info):
    response = {
        'error': reason,
        'status': status_code,
        'timestamp': datetime.datetime.now().timestamp(),
    }

    exception = exception_info[1]
    exception_cls_name = exception.__class__.__name__
    exception_message = exception.log_message if isinstance(exception, HTTPError) else str(exception)
    exception_attr = exception.attr if isinstance(exception, ApplicationException) else None

    response['exception'] = exception_cls_name
    response['attributes'] = exception_attr
    response['message'] = exception_message
    response['errors'] = [{
        'message': exception_message,
        'attributes': exception_attr,
    }]

    return response
