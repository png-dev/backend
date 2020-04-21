# -*- coding: utf-8 -*-

from application.models.base_model import Model
import application.utils as util


class RolePost(Model):
    def __init__(self, id: str = None, permisstion: list = None, desc: str = None):
        self.swagger_type = {
            'id': str,
            'permisstion': list,
            'desc': str
        }

        self.attibute_map = {
            'id': 'id',
            'permisstion': 'permisstion',
            'desc': 'desc'
        }

        self._id = id
        self._permisstion = permisstion
        self._desc = desc

    @classmethod
    def from_dict(cls, dikt) -> 'RolePost':
        return util.deserialize_model(dict, cls)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def permisstion(self) -> list:
        return self._permisstion

    @permisstion.setter
    def permisstion(self, permisstion: list):
        self._permisstion = permisstion

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        self._desc = desc


