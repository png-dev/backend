# -*- coding: utf-8 -*-
from application.models.base_model import Model
import application.utils as util


class PermissionPost(Model):

    def __init__(self, id: str = None, desc: str = None):
        self.swagger_type = {
            'id': str,
            'desc': str
        }

        self.attibute_map = {
            'id': 'id',
            'desc': 'desc'
        }

        self._id = id
        self._desc = desc

    @classmethod
    def from_dict(cls, dikt) -> 'PermissionPost':
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        return self._desc
