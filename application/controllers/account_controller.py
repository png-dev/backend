# -*- coding: utf-8 -*-

from application.db.mongo import MongoWrappers
from application.db.models import AccountModel
from flask import jsonify
import logging


def get_account_list(_size=None, _from=None, _acounting=None, _sort=None, name=None):
    logging.info('get account list')
    account_collection = MongoWrappers(AccountModel.db, AccountModel.table_name)
    _filter = {}
    if not name is None:
        columns = [
            'account_number',
            'first_name',
            'last_name',
            'gender',
            'age',
            'email',
            'address',
            'city',
            'state',
            'employer',
            'balance'
        ]
        _filter = {}
        and_filter_on_all_columns = []
        for i in range(len(columns)):
            column_filter = {}
            if i == 0 or i == 4 or i == 10:
                try:
                    column_filter[columns[i]] = int(name)
                except ValueError:
                    continue
            else:
                column_filter[columns[i]] = {'$regex': name, '$options': 'i'}

            and_filter_on_all_columns.append(column_filter)
        if len(and_filter_on_all_columns) > 0:
            _filter['$or'] = and_filter_on_all_columns
    if not _from:
        _from = 0

    if not _size or _size < 0:
        _size = 10

    if _size > 100:
        _size = 100

    fields = {'_id': False}
    results = account_collection.find(spec=_filter, fields=fields, limit=_size,
                                      skip=_from, sort=_sort)
    count = 0
    if _acounting:
        count = results.count()
    ret = {
        'code': 200,
        'data': [],
        'count': count
    }
    for r in results:
        ret['data'].append(r)

    return jsonify(ret)


def get_one_account(account_number):
    _filter = {'account_number': account_number}
    fields = {'_id': False}
    account_collection = MongoWrappers(AccountModel.db, AccountModel.table_name)
    results = account_collection.find_one(spec=_filter, fields=fields)
    if results is None:
        ret = {
            'code': 400,
            'data': 'account not found'
        }
    else:
        ret = {
            'code': 200,
            'data': results
        }
    return jsonify(ret)


def create_one_account(person):
    account_collection = MongoWrappers(AccountModel.db, AccountModel.table_name)
    account_number = person.get('account_number')
    _filter = {"account_number": account_number}
    results = account_collection.find_one(spec=_filter)

    if results is not None:
        ret = {
            'code': 400,
            'data': 'account exists'
        }
    person_info = {
        'account_number': person.get('account_number'),
        'first_name': person.get('first_name'),
        'last_name': person.get('last_name'),
        'gender': person.get('gender'),
        'age': person.get('age'),
        'email': person.get('email'),
        'address': person.get('address'),
        'city': person.get('city'),
        'state': person.get('state'),
        'employer': person.get('employer'),
        'balance': person.get('balance')
    }

    _result = account_collection.insert(**person_info)
    new_account = account_collection.find_one(spec={'_id': _result})
    ret = {
        'code': 200,
        'inserted_info': {
            'account_number': new_account.get('account_number'),
            'first_name': new_account.get('first_name'),
            'last_name': new_account.get('last_name'),
            'gender': new_account.get('gender'),
            'age': new_account.get('age'),
            'email': new_account.get('email'),
            'address': new_account.get('address'),
            'city': new_account.get('city'),
            'state': new_account.get('state'),
            'employer': new_account.get('employer'),
            'balance': new_account.get('balance')
        }
    }
    return jsonify(ret)


def update_one_account(account_number, person):
    _filter = {'account_number': account_number}
    fields = {'_id': False}
    account_collection = MongoWrappers(AccountModel.db, AccountModel.table_name)
    _sample = account_collection.find_one(spec=_filter, fields=fields)
    if _sample is None:
        ret = {
            'code': 400,
            'data': 'Account not found'
        }
        return jsonify(ret)
    else:
        person_info = {
            'account_number': person.get('account_number'),
            'first_name': person.get('first_name'),
            'last_name': person.get('last_name'),
            'gender': person.get('gender'),
            'age': person.get('age'),
            'email': person.get('email'),
            'address': person.get('address'),
            'city': person.get('city'),
            'state': person.get('state'),
            'employer': person.get('employer'),
            'balance': person.get('balance')
        }
        account_collection.update(spec=_filter, set_doc=person_info)
        ret = {
            'code': 200,
            'data': 'Update success'
        }
    return jsonify(ret)


def delete_one_account(account_number):
    _filter = {'account_number': account_number}
    fields = {'_id': False}
    account_collection = MongoWrappers(AccountModel.db, AccountModel.table_name)
    _sample = account_collection.find_one(spec=_filter, fields=fields)

    if _sample is None:
        ret = {
            'code': 400,
            'data': 'Account not found'
        }
        return jsonify(ret)
    else:
        account_collection.remove(spec=_filter)
        ret = {
            'code': 200,
            'data': 'delete success'
        }
    return jsonify(ret)
