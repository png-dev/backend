# -*- coding: utf-8 -*-
from application.models.user import UserPost
from application.db.mongo import MongoWrappers
from application.db.models import UserModel
import connexion


def login(body):
    body = UserPost.from_dict(connexion.request.get_json())

    user_collection = MongoWrappers(UserModel.db, UserModel.table_name)
    spec = {
        UserModel.Attr.user_name: body.user_name
    }
