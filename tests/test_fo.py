# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_tool
   Description :
   Author :       23mofang
   date：          2020/2/21
-------------------------------------------------
   Change Activity:
                   2020/2/21:
-------------------------------------------------
"""
__author__ = 'Asdil'
from aftool import tool
from aftool import fo

def test_is_exist():
    cmd = 'touch /tmp/test.txt'
    tool.subprocess_check_all(cmd)
    assert fo.is_exist('/tmp/test.txt')
    print('fo.is_exist 通过')


