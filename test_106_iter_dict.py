# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/10-18:54


# 测试用for遍历字典
def test_iterDict():
    user = {
        "name": "zhangsan",
        "age": 23,
        "sex": 24,
        "money": 125.5
    }
    print(user.items())
    print(type(user.items())) #<class 'dict_items'>
    for k, v in user.items():
        print(k, v)


def test_iterDict_2():
    user = {
        "name": "zhangsan",
        "age": 23,
        "sex": 24,
        "money": 125.5
    }
    listUser = [(k, v) for k, v in user.items()]
    print("listUser", listUser)