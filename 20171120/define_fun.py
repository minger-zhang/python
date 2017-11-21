#!/usr/bin/env python
#-*- coding: utf-8 -*-

from enum import Enum,unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender




######define matecalss#####################

class Field(object):
    def __init__(self,name,column_type):
        self.name        = name
        self.colunm_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)


class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')


class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k ,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)


class Model(dict, metaclass = ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init(**kv)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute'%s'" % key)
    def __setattr(self,key,value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args   = []
        for k,v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s(%s) values (%s)' % (self.__table__.','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args)) 



class User(Model):
    id       = InteherField('id')
    name     = StringField('username')
    email    = StringField('email')
    password = StringField('password')























