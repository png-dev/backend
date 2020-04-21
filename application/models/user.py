# -*- coding: utf-8 -*-
from application.models.base_model import Model
import application.utils as util


class UserPost(Model):
    def __init__(self, user_name: str = None, phone: str = None, password: str = None, id: int = None,
                 roles: list = None, country: str = None):
        self.swagger_type = {
            'user_name': str,
            'phone': str,
            'password': str,
            'id': int,
            'roles': list,
            'country': str

        }
        self.attibute_map = {
            'user_name': 'user_name',
            'phone': 'phone',
            'password': 'password',
            'id': 'id',
            'roles': 'roles',
            'country': 'country'
        }

        self._user_name = user_name
        self._phone = phone
        self._password = password
        self._id = id
        self._roles = roles
        self._country = country

    @classmethod
    def from_dict(cls, dikt) -> 'UserPost':
        return util.deserialize_model(dikt, cls)

    @property
    def user_name(self) -> str:
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str):
        self._user_name = user_name

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def roles(self) -> list:
        return self._roles

    @roles.setter
    def roles(self, roles: list):
        self._roles = roles

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country
