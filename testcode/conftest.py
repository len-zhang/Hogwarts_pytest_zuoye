# -*- coding:utf-8 -*-
import pytest
import os
import sys

import yaml

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 将根目录添加到sys path，否则terminal中执行pytest会报错
from sourcecode.calc_code import Calculator


@pytest.fixture(scope="class")
def calc_init():
    print("【开始计算】")
    c = Calculator()
    yield c
    print("【计算结束】")


def get_data():
    with open("./calc_data.yaml", encoding="utf-8") as f:
        all_data = yaml.safe_load(f)
        add_normal_data = all_data['add']['normal']
        add_float_data = all_data['add']['float']
        add_unusual_data = all_data['add']['unusual']
        div_normal_data = all_data['div']['normal']
        div_unusual_data = all_data['div']['unusual']
        sub_normal_data = all_data['sub']['normal']
        sub_float_data = all_data['sub']['float']
        sub_unusual_data = all_data['sub']['unusual']
        mul_normal_data = all_data['mul']['normal']
        mul_unusual_data = all_data['mul']['unusual']
        return [add_normal_data, add_float_data, add_unusual_data, div_normal_data, div_unusual_data,
                sub_normal_data, sub_float_data, sub_unusual_data, mul_normal_data, mul_unusual_data]


@pytest.fixture(params=get_data()[0])
def add_normal_data(request):
    return request.param


@pytest.fixture(params=get_data()[1])
def add_float_data(request):
    return request.param


@pytest.fixture(params=get_data()[2])
def add_unusual_data(request):
    return request.param


@pytest.fixture(params=get_data()[3])
def div_normal_data(request):
    return request.param


@pytest.fixture(params=get_data()[4][:2])
def div_unusual_data1(request):
    return request.param


@pytest.fixture(params=get_data()[4][-1])
def div_unusual_data2(request):
    return request.param


@pytest.fixture(params=get_data()[5])
def sub_normal_data(request):
    return request.param


@pytest.fixture(params=get_data()[6])
def sub_float_data(request):
    return request.param


@pytest.fixture(params=get_data()[7])
def sub_unusual_data(request):
    return request.param


@pytest.fixture(params=get_data()[8])
def mul_normal_data(request):
    return request.param


@pytest.fixture(params=get_data()[9])
def mul_unusual_data(request):
    return request.param
