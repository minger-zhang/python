#!/usr/bin/env python
#-*- coding: utf-8 -*-
import logging
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.WARNING)
#logging.basicConfig(level=logging.ERROR)
from define_fun import FooError
from define_fun import main
import pdb


main()


def foo(s):
    n = int(s)
#debug way1:
   # assert n != 0, 'n is zero!'
#debug way2:
    logging.info('n = %d' % n)
    logging.debug('n = %d' % n)
    logging.warning('n = %d' % n)
    logging.error('n = %d' % n)
    pdb.set_trace()
    return 10 / n
   
def run():
    foo('0')


run()



