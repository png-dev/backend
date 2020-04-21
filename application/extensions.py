from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from helpers.action_logger import ActionLogger

action_logger = ActionLogger()
mongo = PyMongo()
jwt = JWTManager()
