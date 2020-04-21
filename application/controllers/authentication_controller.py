# -*- coding: utf-8 -*-
from application.models.user import UserPost
from application.db.mongo import MongoWrappers
from application.db.models import UserModel
from application.exceptions import BadRequest, Unauthorized
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask import jsonify
import connexion


def login(body):
    body = UserPost.from_dict(connexion.request.get_json())

    user_collection = MongoWrappers(UserModel.db, UserModel.table_name)
    spec = {
        UserModel.Attr.user_name: body.user_name
    }

    user_info = user_collection.find_one(spec=spec)
    if not user_info:
        raise BadRequest(4001007, body.user_name)
    user = UserPost.from_dict(user_info)
    if not check_password_hash(user.password, body.password):
        raise Unauthorized(2000)
    else:
        req = {
            'access_token': create_access_token(identity=body.password)
        }

    result = {
        'detail': 'success',
        'status': 0,
        'data': req
    }
    return jsonify(result)
