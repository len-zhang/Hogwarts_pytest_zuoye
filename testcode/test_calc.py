# -*- coding:utf-8 -*-
import random
import pytest
import yaml
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 将根目录添加到sys path，否则terminal中执行pytest会报错
from sourcecode.calc_code import Calculator

ran_num = random.randint(-100, 100)
div_random_data = (0, ran_num, 0)


def get_data():
    with open("./calc_data.yaml", encoding="utf-8") as f:
        all_data = yaml.safe_load(f)
        add_normal_data = all_data['add']['normal']
        add_float_data = all_data['add']['float']
        add_unusual_data = all_data['add']['unusual']
        div_normal_data = all_data['div']['normal']
        div_unusual_data = all_data['div']['unusual']
        return [add_normal_data, add_float_data, add_unusual_data, div_normal_data, div_unusual_data]


class TestCalc:
    def setup_class(self):
        self.c = Calculator()

    def setup_method(self):
        print("【开始计算】")

    def teardown_method(self):
        print("【计算结束】")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_data()[0])
    def test_add_normal(self, a, b, expect):
        result = self.c.add(a, b)
        assert result == expect

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_data()[1])
    def test_add_float(self, a, b, expect):
        result = self.c.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_data()[2])
    @pytest.mark.xfail(raises=TypeError)  # 预估返回类型错误
    def test_add_unusual(self, a, b, expect):
        result = self.c.add(a, b)
        assert result == expect

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', [div_random_data])
    def test_div_random(self, a, b, expect):
        result = self.c.div(a, b)
        assert result == expect

    @pytest.mark.div
    @pytest.mark.parametrize('a,b', get_data()[4][:2])
    # @pytest.mark.xfail(raises=ZeroDivisionError)
    def test_div_unusual1(self, a, b):
        # result = self.c.div(a, b)
        with pytest.raises(ZeroDivisionError) as e:  # 执行下面的代码时抛异常
            self.c.div(a, b)
        assert e.type == ZeroDivisionError  # 断言抛出的异常类型
        assert "division" in str(e.value)  # 断言抛出异常内容中含有的内容

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', [get_data()[4][-1]])
    @pytest.mark.xfail(raises=TypeError)
    def test_div_unusual2(self, a, b, expect):
        result = self.c.div(a, b)
        assert result == expect


if __name__ == "__main__":
    # print(get_data()[4][-1])
    pytest.main(['test_calc.py', '-v'])
