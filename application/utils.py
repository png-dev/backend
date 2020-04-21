# -*- coding: utf-8 -*-
import six
import typing
import datetime
import os
import yaml


def load_yaml_file(config_file):
    with open(config_file, 'r') as f:
        return yaml.load(f.read())


def need_path_value(yaml_key):
    return yaml_key.endswith('_PATH')


def normpath(path):
    return os.path.normpath(path)


def process_path_value(config_dir, path):
    return normpath(os.path.join(config_dir, path))


def load_config_from_yaml_file(config_file):
    if not os.path.isabs(config_file):
        raise Exception('Config file must be given in absolute form ')
    config_dir = os.path.dirname(config_file)
    config = load_yaml_file(config_file)
    for key in config:
        if need_path_value(key):
            config[key] = process_path_value(config_dir, config[key])
    return config


def update_config_from_enviroment(config):
    for key in config:
        config[key] = os.environ.get(key, config[key])
    return config


def load_config(from_file=None, env=True):
    config = {}
    if from_file is not None:
        config = load_config_from_yaml_file(from_file)
    if env:
        return update_config_from_enviroment(config)
    else:
        return config


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
