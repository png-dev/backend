# -*- coding: utf-8 -*-
import six
import typing
import datetime


def _deserialize_primitive(data, klass):
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    return value


def deserialize_date(string):
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def _deserialize_list(data, boxed_type):
    return [_deserialize(sub_data, boxed_type) for sub_data in data]


def _deserialize_dict(data, boxed_type):
    return {k: _deserialize(v, boxed_type) for k, v in six.iteritems(data)}


def _deserialize(data, klass):
    if data is None:
        return None
    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    elif klass == list:
        return _deserialize_object(data)
    else:
        return deserialize_model(data, klass)


def deserialize_model(data, klass):
    instance = klass()
    if not instance.swagger_type:
        return data
    for attr, attr_type in six.iteritems(instance.swagger_type):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))
    return instance
