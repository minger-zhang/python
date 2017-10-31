#!/usr/bin/env python
#-*- coding: utf-8 -*-

def fact(n):
    if n == 1:
       return 1
    return n*fact(n-1)


def fact1(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
       return product
    return fact_iter(num - 1,num*product)


def print_move(n,a,c):
    print('pang',n,a,'--->',c)
    

def move(n,a,b,c):
    if n == 1:
      # print(a,'-->',c)
      print_move(n,a,c)
    else:
       move(n-1,a,c,b)
       print_move(n,a,c)
       move(n-1,b,a,c)

