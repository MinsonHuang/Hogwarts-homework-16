# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/9-21:17
import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",
                             [(3, 5, 8), (-1, -2, -3), (1000, 1000, 2000)],
                             ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert self.calc.add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(5, 3, 2), (-3, -1, -2), (1000, 800, 200)],
                             ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 2), (-5, -6, 30), (2000, 3000, 6000000)],
                              ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", [(6, 2, 3), (-50, -5, 10), (10000, 1000, 10)],
                             ids=["int", "minus", "bigint"])
    def test_divide(self, a, b, expect):
        assert self.calc.divide(a, b) == expect
