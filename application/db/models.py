from application.extensions import mongo
from application.db.identify import DbTable

from array import array
import pymongo


class BaseDBModel(object):
    db = mongo
    table_name = ''
    attr_type = {}
    allow_sort = {}

    class Attr(object):
        _id = '_id'

    def bin_sort(self, sort):
        if not sort:
            return None
        sort = sort.replace(" ", "").replace('\t', '').replace('\r', '').replace('\n', '').split(',')
        qr_sort = []
        for item in sort:
            type_sort = pymongo.ASCENDING
            key_name = item
            if item.find('-') == 0:
                type_sort = pymongo.DESCENDING
                key_name = item[1: 0]
            if not key_name in self.allow_sort or not self.allow_sort[key_name]:
                continue
            qr_sort.append((key_name, type_sort))
        if not qr_sort:
            return None
        return qr_sort


class AccountModel(BaseDBModel):
    table_name = DbTable.ACCOUNT_MODEL
    attr_type = {
        '_id': str,
        'account_number': int,
        'balance': int,
        'first_name': str,
        'last_name': str,
        'age': int,
        'gender': str,
        'address': str,
        'employer': str,
        'email': str,
        'city': str,
        'state': str

    }

    class Attr(object):
        _id = '_id'
        account_number = 'account_number'
        balance = 'balance'
        first_name = 'first_name'
        last_name = 'last_name'
        age = 'age'
        gender = 'gender'
        address = 'address'
        employer = 'employer'
        email = 'email'
        city = 'city'
        state = 'state'

    allow_sort = {
        Attr._id: True,
        Attr.account_number: True,
        Attr.balance: False,
        Attr.first_name: False,
        Attr.last_name: False,
        Attr.age: False,
        Attr.gender: False,
        Attr.address: False,
        Attr.employer: False,
        Attr.email: False,
        Attr.city: False,
        Attr.state: False
    }

    def __init__(self):
        pass


class UserModel(BaseDBModel):
    table_name = DbTable.USER_MODEL

    attr_type = {
        '_id': str,
        'user_name': str,
        'phone': str,
        'password': str,
        'id': int,
        'roles': array,
        'country': str
    }

    class Attr(object):
        _id = '_id'
        user_name = 'user_name'
        phone = 'phone'
        password = 'password'
        id = 'id'
        roles = 'roles'
        country = 'country'

    allow_sort = {
        Attr._id: True,
        Attr.user_name: True,
        Attr.phone: False,
        Attr.password: False,
        Attr.id: True,
        Attr.roles: False,
        Attr.country: False
    }

    def __init__(self):
        pass


class RolesModel(BaseDBModel):
    table_name = DbTable.ROLE_MODEL

    attr_type = {
        '_id': str,
        'id': str,
        'permisstion': array,
        'desc': str
    }

    class Attr(object):
        _id = '_id'
        permisstion = 'permisstion'
        desc = 'desc'
        id = 'id'

    allow_sort = {
        Attr._id: True,
        Attr.permisstion: True,
        Attr.desc: False,
        Attr.id: True
    }

    def __init__(self):
        pass


class PermisstionModel(BaseDBModel):
    table_name = DbTable.PERMISSTION_MODEL

    attr_type = {
        '_id': str,
        'id': str,
        'desc': str
    }

    class Attr(object):
        _id = '_id'
        desc = 'desc'
        id = 'id'

    allow_sort = {
        Attr._id: True,
        Attr.desc: False,
        Attr.id: True
    }

    def __init__(self):
        pass
