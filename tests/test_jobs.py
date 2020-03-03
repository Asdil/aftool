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
import numpy as np
from aftool import jobs


def test_dump():
    save_path = '/tmp/joblib.tmp.pkl'
    data = np.ones((1000, 1000))
    jobs.dump(data, save_path)


def test_load():
    data_path = '/tmp/joblib.tmp.pkl'
    data = jobs.load(data_path)


def test_parallel():
    data = np.ones((1000, 1000))
    memmap_data = jobs.memmap(data)
    datas = [[i, memmap_data] for i in range(8)]
    ret = jobs.parallel(datas, jobs.test_func, njobs=2)
    for i, d in enumerate(ret):
        assert i == d




