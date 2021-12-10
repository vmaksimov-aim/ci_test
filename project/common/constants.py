from datetime import time, timedelta
from typing import ClassVar


class OAuth2Constants:
    GRANT_TYPE_CODE = 'authorization_code'
    GRANT_TYPE_CREDENTIALS = 'client_credentials'
    GRANT_TYPE_REFRESH_TOKEN = 'refresh_token'


class EnvironmentVariables(object):
    AWS_REGION = 'AWS_REGION'
    AWS_COGNITO_USER_POOL = 'AWS_COGNITO_USER_POOL'
    AWS_COGNITO_CLIENT_ID = 'AWS_COGNITO_CLIENT_ID'
    AWS_COGNITO_ADMIN_USER_POOL = 'AWS_COGNITO_ADMIN_USER_POOL'
    AWS_COGNITO_ADMIN_CLIENT_ID = 'AWS_COGNITO_ADMIN_CLIENT_ID'

    LOGGING_LEVEL = 'APPLICATION_LOGGING_LEVEL'

    DATABASE_HOST = 'DATABASE_HOST'
    DATABASE_PORT = 'DATABASE_PORT'
    DATABASE_NAME = 'DATABASE_NAME'
    DATABASE_USER = 'DATABASE_USER'
    DATABASE_PASS = 'DATABASE_PASS'

    CIPHER_SECRET_KEY = 'CIPHER_SECRET_KEY'

    OPEN_ENERGI_LOGIN = 'OPEN_ENERGI_LOGIN'
    OPEN_ENERGI_PASSWORD = 'OPEN_ENERGI_PASSWORD'

    WALLBOX_ACCOUNT = 'WALLBOX_ACCOUNT'
    WALLBOX_TOKEN = 'WALLBOX_TOKEN'

    TIMEOUT_TOTAL = 'TIMEOUT_TOTAL'
    TIMEOUT_CONNECT = 'TIMEOUT_CONNECT'


class ApplicationConstants:
    PORT: ClassVar[int] = 5000


class DecodeConstants(object):
    UTF8 = 'utf-8'


class ContentType(object):
    ALL = '*/*'
    APPLICATION_XLS = 'application/vnd.ms-excel'
    APPLICATION_ATOM_XML = 'application/atom+xml'
    APPLICATION_FORM_URLENCODED = 'application/x-www-form-urlencoded'
    APPLICATION_JSON = 'application/json'
    APPLICATION_JSON_UTF8 = 'application/json;charset=UTF-8'
    APPLICATION_OCTET_STREAM = 'application/octet-stream'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_PROBLEM_JSON = 'application/problem+json'
    APPLICATION_PROBLEM_JSON_UTF8 = 'application/problem+json;charset=UTF-8'
    APPLICATION_PROBLEM_XML = 'application/problem+xml'
    APPLICATION_RSS_XML = 'application/rss+xml'
    APPLICATION_STREAM_JSON = 'application/stream+json'
    APPLICATION_XHTML_XML = 'application/xhtml+xml'
    APPLICATION_XML = 'application/xml'
    IMAGE_GIF = 'image/gif'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_PNG = 'image/png'
    MULTIPART_FORM_DATA = 'multipart/form-data'
    TEXT_EVENT_STREAM = 'text/event-stream'
    TEXT_HTML = 'text/html'
    TEXT_MARKDOWN = 'text/markdown'
    TEXT_PLAIN = 'text/plain'
    TEXT_XML = 'text/xml'
    TEXT_CSV = 'text/csv'

    JSON_CONTENT_TYPES = {
        APPLICATION_JSON,
        APPLICATION_JSON_UTF8,
    }

    TEXT_CONTENT_TYPES = {
        TEXT_EVENT_STREAM,
        TEXT_HTML,
        TEXT_MARKDOWN,
        TEXT_PLAIN,
        TEXT_XML,
        TEXT_CSV,
    }


class HttpHeaders(object):
    ACCEPT = 'Accept'
    ACCEPT_CHARSET = 'Accept-Charset'
    ACCEPT_ENCODING = 'Accept-Encoding'
    ACCEPT_LANGUAGE = 'Accept-Language'
    ACCEPT_RANGES = 'Accept-Ranges'
    ACCESS_CONTROL_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
    ACCESS_CONTROL_ALLOW_HEADERS = 'Access-Control-Allow-Headers'
    ACCESS_CONTROL_ALLOW_METHODS = 'Access-Control-Allow-Methods'
    ACCESS_CONTROL_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
    ACCESS_CONTROL_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
    ACCESS_CONTROL_MAX_AGE = 'Access-Control-Max-Age'
    ACCESS_CONTROL_REQUEST_HEADERS = 'Access-Control-Request-Headers'
    ACCESS_CONTROL_REQUEST_METHOD = 'Access-Control-Request-Method'
    AGE = 'Age'
    ALLOW = 'Allow'
    AUTHORIZATION = 'Authorization'
    CACHE_CONTROL = 'Cache-Control'
    CONNECTION = 'Connection'
    CONTENT_ENCODING = 'Content-Encoding'
    CONTENT_DISPOSITION = 'Content-Disposition'
    CONTENT_LANGUAGE = 'Content-Language'
    CONTENT_LENGTH = 'Content-Length'
    CONTENT_LOCATION = 'Content-Location'
    CONTENT_RANGE = 'Content-Range'
    CONTENT_TYPE = 'Content-Type'
    COOKIE = 'Cookie'
    DATE = 'Date'
    ETAG = 'ETag'
    EXPECT = 'Expect'
    EXPIRES = 'Expires'
    FROM = 'From'
    HOST = 'Host'
    IF_MATCH = 'If-Match'
    IF_MODIFIED_SINCE = 'If-Modified-Since'
    IF_NONE_MATCH = 'If-None-Match'
    IF_RANGE = 'If-Range'
    IF_UNMODIFIED_SINCE = 'If-Unmodified-Since'
    LAST_MODIFIED = 'Last-Modified'
    LINK = 'Link'
    LOCATION = 'Location'
    MAX_FORWARDS = 'Max-Forwards'
    ORIGIN = 'Origin'
    PRAGMA = 'Pragma'
    PROXY_AUTHENTICATE = 'Proxy-Authenticate'
    PROXY_AUTHORIZATION = 'Proxy-Authorization'
    RANGE = 'Range'
    REFERER = 'Referer'
    RETRY_AFTER = 'Retry-After'
    SERVER = 'Server'
    SET_COOKIE = 'Set-Cookie'
    SET_COOKIE2 = 'Set-Cookie2'
    TE = 'TE'
    TRAILER = 'Trailer'
    TRANSFER_ENCODING = 'Transfer-Encoding'
    UPGRADE = 'Upgrade'
    USER_AGENT = 'User-Agent'
    VARY = 'Vary'
    VIA = 'Via'
    WARNING = 'Warning'
    WWW_AUTHENTICATE = 'WWW-Authenticate'


class HttpStatus:
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    FOUND = 302
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


class AuthorizationData:
    AUTHORIZATION_HEADER = 'Authorization'
    AUTHORIZATION_METHOD = 'Bearer '
    INVALID_HEADER_MESSAGE = 'Invalid authorization header structure!'
    MISSING_AUTHORIZATION_KEY = 'Missing authorization header!'
    AUTHORIZATION_ERROR_MESSAGE = 'Authorization error'

    ALGORITHMS: tuple = ('HS256', 'RS256')
    TOKEN_TYPES: tuple = ('access', 'id')


class OpenEnergiConstants:
    ACTION_BOOST = 'boost'
    ACTION_SCHEDULER = 'scheduler'
    ACTION_IDLE = 'idle'
    HALF_HOUR_TIME = 30


class Octopus:
    ACCOUNT_ID = 'account_id'
    API_KEY = 'api_key'


class DefaultValues:
    ZERO_VALUE = 0
    DECIMAL_PLACES = 2


class TreeConvertDefaults:
    CO2_PER_KM = 0.138  # Emitted by Diesel 1.7l Nissan Qashqai
    KM_PER_KWH = 6.25  # For Nissan Leaf
    CO2_YEARLY_ABSORBED = 22.0  # By average tree
    ZERO_VALUE = 0


class ChargerConstants:
    T_10_MINUTES = timedelta(minutes=10)


class DatabaseConstants:
    MAX_VARCHAR_LENGTH: int = 255


class NissanLeafValues:
    """
    All cars are Nissan Leaf with the same size battery.

    On fully charge 40 kWh Leaf can do 243 kilometers which mean that 1% of charge is 2.43 kilometers.
    On fully charge 62 kWh Leaf can do 385 kilometers which mean that 1% of charge is 3.85 kilometers.
    """
    CONVERSION_KILOMETERS = 'kilometers'
    CONVERSION_MILES = 'miles'

    CONVERSION_CAPACITY_FORTY_KILOMETERS: float = 2.43
    CONVERSION_CAPACITY_FORTY_MILES: float = 1.51

    CONVERSION_CAPACITY_SIXTY_TWO_KILOMETERS: float = 3.85
    CONVERSION_CAPACITY_SIXTY_TWO_MILES: float = 2.4

    CAPACITY_FORTY = 40
    CAPACITY_SIXTY_TWO = 62

    CAPACITY_FORTY_SQL = '40'

    CONVERSION_CONFIGURATION = {
        CAPACITY_FORTY: {
            CONVERSION_KILOMETERS: CONVERSION_CAPACITY_FORTY_KILOMETERS,
            CONVERSION_MILES: CONVERSION_CAPACITY_FORTY_MILES,
        },
        CAPACITY_SIXTY_TWO: {
            CONVERSION_KILOMETERS: CONVERSION_CAPACITY_SIXTY_TWO_KILOMETERS,
            CONVERSION_MILES: CONVERSION_CAPACITY_SIXTY_TWO_MILES,
        },
    }


class ClientTimeout:
    """Default timeout for connection and response in seconds"""

    TOTAL: int = 5 * 60
    CONNECT: int = 30


class SchedulerConstants:
    SCHEDULER_DATE = 'date'
    SCHEDULER_CRON = 'cron'
    SCHEDULER_INTERVAL = 'interval'

    EVENT_SCHEDULER_NOON = 12
    EVENT_SCHEDULER_MIDNIGHT = 00
    DEFAULT_TIME: time = time(hour=5)
    DEFAULT_SOC: int = 80
    TARGET_TIME: str = 'target_time'
    DESIRED_SOC: str = 'desired_soc'
    MISFIRE_GRACE_TIME: int = 60
    MAX_INSTANCES: int = 10


class ImpersonatedVariables:
    IMPERSONATING_SUB = 'impersonating_sub'
    IMPERSONATING_EMAIL = 'impersonating_email'
    IMPERSONATED_BY_SUB = 'impersonated_by_sub'
    IMPERSONATED_BY_EMAIL = 'impersonated_by_email'
