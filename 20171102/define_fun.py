#!/usr/bin/env python
#-*- coding: utf-8 -*-
import functools

####################varargs sum
def cacl_sum(*args):
     ax = 0
     for n in args:
         ax = ax + n
     return ax
################### closure include varargs
def lazy_sum(*args):
     def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
     return sum


#################count() && count1() define a function to use circle argument
#################   
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

###################
def count1():
    def f(j):
        return lambda :j*j
    fs = []
    for i in range(1,4):
       fs.append(f(i))
    return fs

######################################################################
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return  decorator


@log('execute')
def now():
    print('2017-11-02')


#########################################################################
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return (func(*args,**kw),print('end call %s()' % func.__name__))
        return wrapper
    return decorator

@log1('begin call') #####test_now = log(begin call)(test_now)
def test_now():
    print('2017-11-02')


#######################################
def log2():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call')
 #           if text == None:
 #               print('call = %s()' % func.__name__)
 #           else:
  #              print('text = %s\ncall = %s()' % (text,func.__name__))
            f = func(*args,**kw)
 #           func(*args,**kw)
            print('end call')
            return f
#            return func(*args,**kw)
        return wrapper
    return decorator


@log2()
def test_now1():
    print('2017-11-02')


########################################################################
def log3(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kw):
        print('begin %s' % fun.__name__)
        fun(*args,**kw) 
        print('end %s' % fun.__name__)
    return wrapper


@log3
def test_now3():
    print('2017-11-02')


def log4(text = None):
    def decorator(func):
        def wrapper(*args,**kw):
            print('call begin %s' % text)
            func(*args,**kw)
            print('call end %s' % text)
        return wrapper
    return decorator


@log4()
def test_now4():
    print('2017-11-02')

@log4('execute')
def test_now5():
    print('2017-11-02')



###########################################################################
########################partial function###################################
def int2(x,base=2):
    return int(x,base)




  
