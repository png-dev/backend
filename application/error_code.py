# -*- coding: utf-8 -*-

HTTP_STATUS_CODES = {
    # 1×× Informational
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',

    # 2×× Success
    200: 'Ok',
    201: 'Created',
    202: "Accepted",
    203: "Non Authoritative Information",
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi Status',
    226: 'IM Used',

    # 3×× Redirection
    300: 'Multiple Choises',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',

    # 4×× Client Error
    400: 'Bad Request',
    401: 'Anauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'Request-URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    418: "I'm a teapot",
    421: 'Misdirected Request',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    431: 'Request Header Field Too Large',
    444: 'Connection Closed Without Response',
    451: 'Unavailable For Legal Reasons',
    499: 'Client Closed Request',

    # 5xx Server Error
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required',
    599: 'Network Connect Timout Error'
}

HTTP_100_CONTINUE = {
}
HTTP_101_SWITCHING_PROTOCOLS = {
}
HTTP_102_PROCESSING = {
}

HTTP_100_CONTINUE = {
}
HTTP_101_SWITCHING_PROTOCOLS = {
}
HTTP_200_OK = {
}
HTTP_201_CREATED = {
}
HTTP_202_ACCEPTED = {
}
HTTP_203_NON_AUTHORITATIVE_INFORMATION = {
}
HTTP_204_NO_CONTENT = {
}
HTTP_205_RESET_CONTENT = {
}
HTTP_206_PARTIAL_CONTENT = {
}
HTTP_300_MULTIPLE_CHOICES = {
}
HTTP_301_MOVED_PERMANENTLY = {
}
HTTP_302_FOUND = {
}
HTTP_303_SEE_OTHER = {
}
HTTP_304_NOT_MODIFIED = {
}
HTTP_305_USE_PROXY = {
}
HTTP_306_RESERVED = {
}
HTTP_307_TEMPORARY_REDIRECT = {
}
HTTP_400_BAD_REQUEST = {
    1001: 'Not login!',
    1002: 'Content-Type in request header is not \'application/json\'!',
    1003: 'Missing field in request!',
    1004: '',
    1005: 'Duplicated metadata',
    1006: 'Metadata does not exist',
    1007: 'Parent does not exist',
    1008: 'Please delete child of this metadata first',
    1009: 'Invalid param {0}',
    1010: 'Value of param {0} has already existed',
    # Report & data template error code
    1100: 'Arguments validation error',
    1101: 'Template does not exist',
    1102: 'Template name \'{0}\' has already existed',
    1103: 'Report name \'{0}\' has already existed',
    1104: 'Report does not exist',
    1105: 'Data template is used for report \'{0}\'. Please delete report first',
    1106: 'Data source \'{0}\' is not supported',
    1107: 'Can not edit or delete data template of other user',
    1108: 'Can not edit or delete report of other user',
    # Reporting error code
    1200: 'Parameter \'{0}\' is invalid',
    1201: 'Database \'{0}\' does not exist',
    1202: 'Aggregation failed',
    1203: 'Database \'{0}\' is not supported',
    1204: 'Collection \'{0}\' is not supported',
    1205: 'Filter field \'{0}\' is invalid',
    1206: 'Error while casting field \'{0}\' to \'{1}\'',
    1207: 'Data type \'{0}\' is not supported',
    1208: 'Missing reporting directory in configuration file',
    1209: 'Reporting directory does not exist',
    1210: 'Reporting history not found',
    1211: 'File not found',
    1212: 'Error while saving pdf file',
    # History error code
    1250: 'Report history does not exist',
    4000000: "Invalid Parameter",
    4001000: "Parameter {} is invalid",
    4001001: "{} has already existed",
    4001002: "{} has not existed",
    4001003: "Parameter {} in properties is required",
    4001004: "Parameter {} is not allowed to search regex",
    4001005: "Parameter {} is not a json string",
    4001006: "Sum of {}, {} is greater than {}",
    4001007: "{} has not existed",
    4001008: "Parameter {} is wrong format",
}
HTTP_401_UNAUTHORIZED = {
    2000: 'Authentication Failed: Wrong username or password.'
}
HTTP_402_PAYMENT_REQUIRED = {
    3000: ''
}
HTTP_403_FORBIDDEN = {
    4000: 'Access denied!'
}
HTTP_404_NOT_FOUND = {
}
HTTP_405_METHOD_NOT_ALLOWED = {
}
HTTP_406_NOT_ACCEPTABLE = {
}
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = {
}
HTTP_408_REQUEST_TIMEOUT = {
}
HTTP_409_CONFLICT = {
}
HTTP_410_GONE = {
}
HTTP_411_LENGTH_REQUIRED = {
}
HTTP_412_PRECONDITION_FAILED = {
}
HTTP_413_REQUEST_ENTITY_TOO_LARGE = {
}
HTTP_414_REQUEST_URI_TOO_LONG = {
}
HTTP_415_UNSUPPORTED_MEDIA_TYPE = {
}
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = {
}
HTTP_417_EXPECTATION_FAILED = {
}
HTTP_422_UNPROCESSABLE_ENTITY = {
    42201: 'Rule name: {0} already exists',
    42202: 'Metadata: {0} - {1} already exists',
    42203: 'Language: {0} already exists'
}
HTTP_428_PRECONDITION_REQUIRED = {
}
HTTP_429_TOO_MANY_REQUESTS = {
}
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = {
}
HTTP_500_INTERNAL_SERVER_ERROR = {
    5000000: 'Internal server error',
    5001000: 'File does not exist',
    5001010: "Redis connection error"
}
HTTP_501_NOT_IMPLEMENTED = {
}
HTTP_502_BAD_GATEWAY = {
}
HTTP_503_SERVICE_UNAVAILABLE = {
}
HTTP_504_GATEWAY_TIMEOUT = {
}
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = {
}
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = {
}
