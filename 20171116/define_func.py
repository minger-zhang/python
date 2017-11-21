#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Person(object):
    pass

class Student(Person):
    __slots__=('name','age')

###'Student1' object counld not accept another attribute 
class Person1(object):
    __slots__=()

class Student1(Person1):
    __slots__=('name','age')


class Student2(object):
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

##############@property############################
class Student3(object):
    
    @property
    def score(self):
        return self._score
 

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('socre must be an interger!')
        if value < 0 or value > 100:
           raise ValueError('score must between 0 ~100!')
        self._score = value

class Student4(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value


    @property
    def age(self):
        return 2017 - self._birth





class Screen(object):
 
    @property
    def width(self):
        return self._width
  
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 10000:
            raise ValueError('score must between 0~10000')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 10000:
            raise ValueError('score must between 0~10000')
        self._height = value

    @property
    def resolution(self):
         return self._width * self._height

  










