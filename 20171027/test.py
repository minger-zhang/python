#!/usr/bin/env python
#-*- coding: utf-8 -*-

print(r'''She
is
a
beautiful
girl!''')
####test 1 just print

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r''' hello,
Lisa!'''

print('n = ',n)
print('f = ',f)
print('s1 = ',s1)
print('s2 = ',s2)
print('s3 = ',s3)
print('s4 = ',s4)



###test part string & encode decode

s1 = 72
s3 = 85

r = (85 - 72) / 72 * 100

print('grow rate:%.1f%%' % r)



##test part list && tuple
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print('Apple = ', L[0][0])
print('Python = ', L[1][1])
print('Lisa = ', L[2][2])


###test age atuomic test
print(' please enter Height(m):')
s = input()
height = float(s)

print('please enter Weight(KG):')
s = input()
weight = float(s)

bmi = weight / (height * height)

if bmi < 18.5:
	print('too light')
elif 18.5 <= bmi < 25:
	print('normal')
elif 25 <= bmi < 28:
	print('too weight')
elif 28 <= bmi < 32:
	print('fat')
else:
	print('too fat')


##circulate calculation

names = ['Micheal', 'Bob', 'Tracy']
for name in names:
	print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)

sum = 0
for x in list(range(101)):
	sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello,%s!' % name)
