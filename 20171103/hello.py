#!/usr/bin/env python
#-*- coding:utf-8-*-

'a test module'               ###Modules documentation comments
 
__author__ = 'Minger Zhang'   ###Modules author
 

import sys                    ###impor buildin modules 

def test():
    args = sys.argv           ####sys modules include argv argument
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()







