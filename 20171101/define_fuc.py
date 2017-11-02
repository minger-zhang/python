#!/usr/bin/env python
#-*- coding: utf-8 -*-
from functools import reduce


def add(x,y,f):
     return f(x) + f(y)

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name

def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L) 

def str2float(s):
    
    s = s.split('.')
    def str2num(str):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[str]
    def f1(x,y):
        return x * 10 + y
    def f2(x,y):
        return x / 10 +y
					            ######turn list with [::-1]
    return reduce(f1,map(str2num,s[0])) + reduce(f2,list(map(str2num,s[1]))[::-1]) / 10



def str22float(s):
    s = s.split('.')
    def str2num(str):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[str]
   
    return reduce(lambda x,y:x * 10 + y,map(str2num,s[0])) + reduce(lambda x,y:x/10+y,list(map(str2num,s[1]))[::-1]) /10




############################filter#####################################
def is_odd(n):
      return n%2 == 1

#######strip delete space in string(head & tail)
def not_empty(s):
      return s and s.strip()


#######define primes
def _ood_iter():
     n = 1
     while True:
         n = n + 2
         yield n

def _not_divisible(n):
     return lambda x:x%n > 0

def primes():
    yield 2
    it = _ood_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

########palindrome
def is_palindrome(n):
    n  = list(str(n))
    for i in range(len(n)):
        return len(n) > 1 and n[i] == n[len(n) - 1]

def is_palindrome2(n):
    return n == int(str(n)[::-1])

#########sorted by name || by score
def by_name(t):
        return t[0]

def by_score(t):
       return t[1]


##################return function
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum





























