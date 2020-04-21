# -*- coding: utf-8 -*-

from application.error_code import *
from werkzeug.exceptions import HTTPException
from flask import current_app, jsonify


def http_status_message(status_code):
    return HTTP_STATUS_CODES.get(status_code, '')


def error_data(error_code, message, params=''):
    if params:
        params = ','.join(params)
    else:
        params = ''
    error = {
        'status_code': error_code,
        'detail': message,
        'params': params
    }
    return error


def get_error_message(data):
    try:
        messges = data['messages']
        for k, v in messges.items():
            if isinstance(v, dict):
                for ik, iv in v.items():
                    if isinstance(iv, list) and iv:
                        return iv[0]
                    elif isinstance(iv, str):
                        return iv
            elif isinstance(v, str):
                return v
            else:
                return 'Validation error, re-check your data'
    except Exception:
        return 'Validation error, re-check your data'


def api_error_handler(error):
    if isinstance(error, HTTPException):
        code = error.code
        if not isinstance(error.description, dict):
            if code == 422:
                data = getattr(error, 'data')
                error.description = error_data(code, get_error_message(data))
            else:
                error.description = error_data(code, http_status_message(code))
    elif isinstance(error, APIException):
        code = error.status_code
    else:
        code = 500
        error.description = error(code, http_status_message(code))
    msg = 'HTTP_STATUS_CODE_{0}: {1}'.format(code, error.description)
    if code != 404:
        current_app.logger.error(msg, exec_info=error)
    return jsonify(error.description), code


class APIException(Exception):
    status_code = 500
    http_status_code = HTTP_500_INTERNAL_SERVER_ERROR
    params = []

    def __init__(self, error_code=None, *args):
        if error_code in self.http_status_code:
            self.error_code = error_code
        else:
            self.error_code = self.status_code
        message = self.http_status_code \
            .get(error_code, http_status_message(self.status_code))
        self.message = message.format(*args)
        self.params = args

    @property
    def description(self):
        return error_data(self.error_code, self.message, self.params)


class BadRequest(APIException):
    status_code = 400
    http_status_code = HTTP_400_BAD_REQUEST


class Unauthorized(APIException):
    status_code = 401
    http_status_code = HTTP_401_UNAUTHORIZED


class Forbidden(APIException):
    status_code = 403
    http_status_code = HTTP_403_FORBIDDEN


class NotFound(APIException):
    status_code = 404
    http_status_code = HTTP_404_NOT_FOUND


class MethodNotAllowed(APIException):
    status_code = 405
    http_status_code = HTTP_405_METHOD_NOT_ALLOWED


class NotAcceptable(APIException):
    status_code = 406
    http_status_code = HTTP_406_NOT_ACCEPTABLE


class Conflict(APIException):
    status_code = 409
    http_status_code = HTTP_409_CONFLICT


class OverLimit(APIException):
    status_code = 413
    http_status_code = HTTP_413_REQUEST_ENTITY_TOO_LARGE


class UnsupportedMediaType(APIException):
    status_code = 415
    http_status_code = HTTP_415_UNSUPPORTED_MEDIA_TYPE


class UnprocessableEntity(APIException):
    status_code = 422
    http_status_code = HTTP_422_UNPROCESSABLE_ENTITY


class RateLimit(APIException):
    status_code = 429
    http_status_code = HTTP_429_TOO_MANY_REQUESTS


class InternalServerError(APIException):
    status_code = 500
    http_status_code = HTTP_500_INTERNAL_SERVER_ERROR
