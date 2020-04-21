from enum import Enum
from flask import request


class ActionLogger(object):
    def __init__(self, app=None, logger=None):
        if app is not None and logger is not None:
            self.init_app(app, logger)

    def init_app(self, app, logger):
        self.logger = logger
        self.enable = app.config.get('ACTION_LOG_ENABLED', True)
        self.action_log_default_actor = app.config.get('ACTION_LOG_DEFAULT_ACTOR', 'action_logger')

    def get_actor(self):
        actor = request.args.get('actor', default=None)
        if actor is None:
            body = request.get_json()
            if body is not None:
                actor = body.get('actor', None)
        return actor


