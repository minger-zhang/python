#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hello
from define_fun import greeting
from define_fun import Student
from define_fun import Student1
from define_fun import Dog
from define_fun import Cat



hello.test() #####can't bring argument

print(greeting('Minger'))
print(greeting('A'))

###############################################test class
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
bart.name = 'Minger'
bart.score = 100
bart.print_score()


minger = Student1('Minger Zhang',100)
minger.print_score()

#print(minger.__name)
print(minger.get_name())
print(minger.get_score())
minger.set_score(90)
print(minger.get_score())
minger._Student1__name = 'Mike'
print(minger.get_name())


################################################################
dog = Dog()
dog.run()

cat = Cat()
cat.run()


















