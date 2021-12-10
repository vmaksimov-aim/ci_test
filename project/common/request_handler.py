import json
from typing import Dict, Optional

from powerloop.common.base_request_handler import BaseRequestHandler
from powerloop.common.constants import ContentType, HttpHeaders
from powerloop.common.exceptions import NotFoundException, RequestValidationException
from powerloop.common.pagination import Pageable
from powerloop.configuration.validator import create_validator


class JsonRequestHandler(BaseRequestHandler):
    validator = create_validator()

    get_validator_data: dict = None
    post_validator_data: dict = None
    patch_validator_data: dict = None
    put_validator_data: dict = None

    default_page: int = 1
    default_page_size: int = 20
    default_page_sort: str = None

    pageable: Optional[Pageable]
    json_body: Optional[Dict]

    def write_response(self, response):
        if isinstance(response, (list, tuple, dict)):
            self.write_as_json(response)

    def set_default_headers(self):
        super().set_default_headers()
        self.set_header(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON)

    def prepare(self):
        self._create_request_id()
        request_method = self.request.method.lower()

        method_name = f'prepare_{request_method}_request'
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            method()

    def prepare_post_request(self):
        self._prepare_data_request()

    def prepare_patch_request(self):
        self._prepare_data_request()

    def prepare_put_request(self):
        self._prepare_data_request()

    def prepare_delete_request(self):
        self._prepare_data_request()

    def prepare_get_request(self):
        self._create_request_id()
        page = self.get_query_argument('page', str(self.default_page))
        size = self.get_query_argument('size', str(self.default_page_size))

        page = int(page) if page.isdigit() else None
        page_size = int(size) if size.isdigit() else None

        if page or page_size:
            self.pageable = Pageable(
                page=page,
                size=page_size,
            )

    def write_as_json(self, response):
        if isinstance(response, (list, tuple)) and not response:
            response = []
        elif isinstance(response, dict) and not response:
            response = {}

        response = response if response is not None else {}
        self.write(json.dumps(response))

    def _prepare_data_request(self):
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                request_method = self.request.method.lower()
                normalized_data = None
                validator_data = None

                method_name = f'{request_method}_validator_data'
                if hasattr(self, method_name):
                    validator_data = getattr(self, method_name)

                if validator_data and json_data:
                    self._validate_request(json_data, validator_data)
                    normalized_data = self.validator.normalized(json_data, schema=validator_data)

                self.json_body = normalized_data if normalized_data else json_data
            except RequestValidationException as error:
                raise RequestValidationException(error.log_message)
            except Exception as error:
                raise RequestValidationException(str(error))


class NotFoundRequestHandler(JsonRequestHandler):

    def prepare(self):
        raise NotFoundException('Endpoint not found')
