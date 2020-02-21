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


def test_inter_set():
    l1 = [1,2,3,4,5]
    l2 = [4,5,6,7,8]
    inter_l1_l2 = tool.inter_set(l1,l2)
    assert len(inter_l1_l2) == 2
