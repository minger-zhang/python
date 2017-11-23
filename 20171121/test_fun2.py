#!/usr/bin/env python
#-*- coding:utf-8-*-
import platform

class Dict2(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict2()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict2(a=1,b=2,c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ....
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ....
    AttributeError: 'Dict2' object has no attribute 'empty'
    '''

    def __init__(self,**kw):
        if platform.python_version() == '2.7.3':
            super(Dict2,self).__init__(**kw)
        else:
            super().__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict2' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value



if __name__ == '__main__':
    import doctest
    doctest.testmod()




