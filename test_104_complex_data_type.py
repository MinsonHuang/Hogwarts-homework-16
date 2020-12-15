# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/10-17:40


# 测试复数类 <class 'complex'>
def test_complexDataType_1():
    a = 5 + 6j
    print(type(a))
    print("a.real:", a.real)
    print("a.imag:", a.imag)

    # 测试复数的加减
    b = 1 - 2j
    c = a + b
    print("c.real:", c.real)
    print("c.imag", c.imag)