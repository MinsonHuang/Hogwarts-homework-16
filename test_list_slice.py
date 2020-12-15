# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/10-17:35


# 测试列表的切片
def test_listSlice():
    listOne = [1, 2, 3, 4, 5]
    listTwo = listOne[-3:-1:2]
    print("listTwo:", listTwo)