#!/usr/bin/env python
#-*- coding: utf-8 -*-
from define_fuc import add
from define_fuc import normalize
from define_fuc import prod
from define_fuc import str2float
from define_fuc import str22float
from define_fuc import is_odd
from define_fuc import not_empty
from define_fuc import primes
from define_fuc import is_palindrome
from define_fuc import is_palindrome2
from define_fuc import by_name
from define_fuc import by_score
from define_fuc import lazy_sum


####################map / reduce #############################
#########test normalize
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)

########test prod
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#######test str2float
print('str2float(\'123.456\') =', str2float('123.456'))

#####test str22float
print('str22float(\'123.456\') =', str22float('123.456'))


######test is_odd
L1 = list(filter(is_odd,[1,2,4,5,6,9,10,15]))
print(L1)

#######test not_empty
L1 = list(filter(not_empty,['A','','B',None,'C',' ']))
print(L1)


#######test primes
for n in primes():
      if n < 1000:
         print(n)
      else:
         break

############test palindrome
output = filter(is_palindrome,range(1,1000))
print(list(output))

output2 = filter(is_palindrome2,range(1,1000))
print(list(output2))


##########test by_name
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L,key=by_score)
print(L3)

##########################return funtion######################
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())










