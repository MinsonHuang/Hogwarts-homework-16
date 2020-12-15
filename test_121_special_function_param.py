# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/15-16:40


# 测试仅可以传递位置参数的函数形参定义
def func_1(a, b, /):
    print("a:", a)
    print("b:", b)


def test_only_postion_param():
    func_1(1, 2)
    func_1(1, b=2)  # TypeError: func_1() got some positional-only arguments passed as keyword arguments: 'b'


# 测试仅可以传递关键字参数的函数形参定义
def func_2(*, a):
    print("a:", a)


def test_only_key_word_param():
    func_2(a=3)
    func_2(2)  # TypeError: func_2() takes 0 positional arguments but 1 was given


# 测试各种特殊参数组合在一起
def func_3(position_only, / , standard, *, key_word_only):
    print("position_only", position_only)
    print("standard", standard)
    print("key_word_only", key_word_only)


def test_all_special_param():
    func_3(1, 2, key_word_only=5)
    func_3(1, standard=2, key_word_only=5)
    # func_3(position_only=1, standard=2, key_word_only=5) #报错只能传递位置参数的形参，却传递了关键字参数
    # func_3(1, standard=2, 5)  # 报错，位置参数在关键字参数后面了，positional argument follows keyword argument


# 测试可以接受任意个参数的参数列表形参
def any_param_list(*any_param):
    for i in any_param:
        print(i)


def test_any_param_list():
    any_param_list(1, 5, 3, 7)
    any_param_list(1, 5, 3, 7, 9)


#  测试可以接受任意个关键字参数的字典形参
def any_key_word_param(**any_key_word_param):
    for (k, v) in any_key_word_param.items():
        # print(k, v)
        print(k, ":", v)
        # print("%s:%s" %(k,v))

def test_any_key_word_param():
    any_key_word_param(a=1, b=2, c=3)


