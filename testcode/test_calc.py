# -*- coding:utf-8 -*-
import random
import pytest

ran_num = random.randint(-100, 100)
random_data = (0, ran_num, 0)


# def setup_class(self):
#     self.c = Calculator()

# def setup_method(self):
#     print("【开始计算】")
#
# def teardown_method(self):
#     print("【计算结束】")


@pytest.mark.add
@pytest.mark.run(order=1)
class TestAdd:  # 加法的测试类
    def test_add_normal(self, calc_init, add_normal_data):
        result = calc_init.add(add_normal_data[0], add_normal_data[1])
        assert result == add_normal_data[2]

    def test_add_float(self, calc_init, add_float_data):
        result = calc_init.add(add_float_data[0], add_float_data[1])
        assert round(result, 2) == add_float_data[2]

    @pytest.mark.xfail(raises=TypeError)  # 预估返回类型错误
    def test_add_unusual(self, calc_init, add_unusual_data):
        result = calc_init.add(add_unusual_data[0], add_unusual_data[1])
        assert result == add_unusual_data[2]


@pytest.mark.div
@pytest.mark.run(order=4)
class TestDiv:  # 除法的测试类
    def test_div_normal(self, calc_init, div_normal_data):
        result = calc_init.div(div_normal_data[0], div_normal_data[1])
        assert result == div_normal_data[2]

    @pytest.mark.parametrize('a,b,expect', [random_data])
    def test_div_random(self, calc_init, a, b, expect):
        result = calc_init.div(a, b)
        assert result == expect

    def test_div_unusual1(self, calc_init, div_unusual_data1):
        with pytest.raises(ZeroDivisionError) as e:  # 执行下面的代码时抛异常
            calc_init.div(div_unusual_data1[0], div_unusual_data1[1])
        assert e.type == ZeroDivisionError  # 断言抛出的异常类型
        assert "division" in str(e.value)  # 断言抛出异常内容中含有的内容

    @pytest.mark.xfail(raises=TypeError)
    def test_div_unusual2(self, calc_init, div_unusual_data2):
        result = calc_init.div(div_unusual_data2[0], div_unusual_data2[0])
        assert result == div_unusual_data2[0]


@pytest.mark.sub
@pytest.mark.run(order=2)
class TestSub:  # 减法的测试类
    def test_sub_normal(self, calc_init, sub_normal_data):
        result = calc_init.sub(sub_normal_data[0], sub_normal_data[1])
        assert result == sub_normal_data[2]

    def test_sub_float(self, calc_init, sub_float_data):
        result = calc_init.sub(sub_float_data[0], sub_float_data[1])
        assert round(result, 2) == sub_float_data[2]

    @pytest.mark.xfail(raises=TypeError)  # 预估返回类型错误
    def test_sub_unusual(self, calc_init, sub_unusual_data):
        result = calc_init.sub(sub_unusual_data[0], sub_unusual_data[1])
        assert result == sub_unusual_data[2]


@pytest.mark.mul
@pytest.mark.run(order=3)
class TestMul:  # 乘法的测试类
    def test_mul_normal(self, calc_init, mul_normal_data):
        result = calc_init.mul(mul_normal_data[0], mul_normal_data[1])
        assert result == mul_normal_data[2]

    @pytest.mark.parametrize('a,b,expect', [random_data])
    def test_mul_random(self, calc_init, a, b, expect):
        result = calc_init.mul(a, b)
        assert result == expect

    @pytest.mark.xfail(raises=TypeError)
    def test_mul_unusual(self, calc_init, mul_unusual_data):
        result = calc_init.mul(mul_unusual_data[0], mul_unusual_data[0])
        assert result == mul_unusual_data[0]


if __name__ == "__main__":
    pytest.main(['test_calc.py', '-vs'])
