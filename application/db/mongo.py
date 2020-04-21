# -*- coding: utf-8 -*-

class MongoWrappers(object):
    def __init__(self, mongo, collection):
        self.db = mongo.db[collection]

    @staticmethod
    def is_dict(params):
        rv = isinstance(params, dict)
        if not rv:
            raise ValueError('%s is not of type %s ' % (params, dict))
        return params

    def has_object(self, spec):
        spec = self.is_dict(spec)
        if self.db.find_one(spec):
            return True
        return False

    def find(self, spec, fields=None, skip=0, limit=0, sort=None):
        spec = self.is_dict(spec)
        return self.db.find(filter=spec, projection=fields, skip=skip, limit=limit, sort=sort)

    def find_one(self, spec, fields=None):
        spec = self.is_dict(spec)
        return self.db.find_one(filter=spec, projection=fields)

    def insert(self, **kwargs):
        return self.db.insert(kwargs)

    def remove(self, spec):
        spec = self.is_dict(spec)
        return self.db.remove(spec)

    def update(self, spec, set_doc=None, pull_doc=None, push_doc=None, inc_doc=None, unset_doc=None, upsert=False):
        spec = self.is_dict(spec)
        update_doc = {}
        if set_doc:
            update_doc['$set'] = self.is_dict(set_doc)
        if pull_doc:
            update_doc['$pull'] = self.is_dict(pull_doc)
        if push_doc:
            update_doc['$push'] = self.is_dict(push_doc)
        if inc_doc:
            update_doc['$inc'] = self.is_dict(inc_doc)
        if unset_doc:
            update_doc['$unset'] = self.is_dict(unset_doc)
        return self.db.update(spec, update_doc, upsert=upsert)

    def muilti_update(self, spec, set_doc=None, pull_doc=None, push_doc=None, inc_doc=None, unset_doc=None):
        spec = self.is_dict(spec)
        update_doc = {}
        if set_doc:
            update_doc['$set'] = self.is_dict(set_doc)
        if pull_doc:
            update_doc['$pull'] = self.is_dict(pull_doc)
        if push_doc:
            update_doc['$push'] = self.is_dict(push_doc)
        if inc_doc:
            update_doc['$inc'] = self.is_dict(inc_doc)
        if unset_doc:
            update_doc['$unset'] = self.is_dict(unset_doc)
        return self.db.update(spec, update_doc, multi=True)

    def multi_remove(self, spec, doc):
        spec = self.is_dict(spec)
        doc = self.is_dict(doc)
        return self.db.update(spec, {'$pull': doc}, multi=True)

    def multi_append(self, spec, doc):
        spec = self.is_dict(spec)
        doc = self.is_dict(doc)
        return self.db.update(spec, {'$push': doc}, multi=True)

    def multi_increase(self, spec, doc, upsert=False):
        spec = self.is_dict(spec)
        doc = self.is_dict(doc)
        return self.db.update(spec, {'$inc': doc}, upsert=upsert)

    def aggregate(self, pipline):
        return self.db.aggregate(pipline)

    def drop(self):
        self.db.drop()
