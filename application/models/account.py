# -*- coding: utf-8 -*-
from application.models.base_model import Model
import application.utils as util


class AccountPost(Model):
    def __init__(self, account_number: int = None, balance: int = None, first_name: str = None, last_name: str = None,
                 age: int = None, gender: str = None, address: str = None, employer: str = None, email: str = None,
                 city: str = None, state: str = None):
        self.swagger_type = {
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

        self.attibute_map = {
            'account_number': 'account_number',
            'balance': 'balance',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'age': 'age',
            'gender': 'gender',
            'address': 'address',
            'employer': 'employer',
            'email': 'email',
            'city': 'city',
            'state': 'state'
        }

        self._account_number = account_number
        self._balance = balance
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._gender = gender
        self._address = address
        self._employer = employer
        self._email = email
        self._city = city
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'AccountPost':
        return util.deserialize_model(dikt, cls)

    @property
    def account_number(self) -> int:
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: int):
        self._account_number = account_number

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, balance: int):
        self._balance = balance

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_nmae: str):
        self._last_name = last_nmae

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        self._gender = gender

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @property
    def employer(self) -> str:
        return self._employer

    @employer.setter
    def employer(self, employer: str):
        self._employer = employer

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state
