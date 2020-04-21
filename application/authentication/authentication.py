# -*- coding: utf-8 -*-
from functools import wraps


def user_has(permistion):
    def wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            return f(*args, **kwargs)

        return inner

    return wrapper
