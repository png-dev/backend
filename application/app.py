# -*- coding: utf-8 -*-
from werkzeug.exceptions import default_exceptions
from application.exceptions import api_error_handler
from application.extensions import mongo, jwt, action_logger
from application.utils import load_config
import logging
import os
import connexion
import logging.config
module_dir = os.path.dirname(os.path.abspath(__file__))


def configure_error_handlers(app):
    for exception in default_exceptions:
        app.register_error_handler(exception, api_error_handler)
    app.register_error_handler(Exception, api_error_handler)


def configure_extensions(app):
    mongo.init_app(app)
    action_logger.init_app(app, logging.getLogger('action'))
    jwt.init_app(app)


def configure_log_handlers(app):
    logging.config.fileConfig(app.config['LOGGER_CONFIG_PATH'])
    logger = logging.getLogger('root')

    for h in logger.root.handlers:
        app.logger.addHandler(h)

    app.logger.setLevel(logger.root.level)

    app.logger.info('Start api services info log')


def configure_app(app):
    configure_log_handlers(app)
    configure_extensions(app)
    configure_error_handlers(app)


def create_app(config=None):
    app_config = config
    if app_config is None:
        config_file = os.path.join(module_dir, 'config.yaml')
        if os.path.isfile(config_file):
            app_config = load_config(config_file)
        else:
            raise Exception('No valid configuration found')

    swagger_file = app_config.get('SWAGGER_FILE_PATH')
    if swagger_file:
        swagger_dir, swagger_file_name = os.path.split(swagger_file)
        app = connexion.App(__name__, specification_dir=swagger_dir)
        app.add_api(swagger_file_name)
    else:
        raise Exception('SWAGGER_FILE_PATH is required in configuration file')
    flask_app = app.app
    flask_app.config.from_mapping(app_config)
    flask_app.instance_path = module_dir
    configure_app(flask_app)
    return flask_app


