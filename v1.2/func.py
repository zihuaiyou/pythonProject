#
# 这是主界面123主程序文件所需的外部程序文件

# 将字符串型列表转化为浮点型列表的方法
def float_list(list):
    new_list = [float(x) for x in list]
    return new_list


# 将列表转化为字符串型列表的方法
def str_list(list):
    new_list = [str(x) for x in list]
    return new_list


# 确定列表中重复元素个数
def countX(list, x):
    return list.count(x)


def quadratic(a, b, c):
    import math
    # 二次方程情况
    if int(a) != 0:
        key = b ** 2 - 4 * a * c
        if key > 0:
            x1 = (-b + math.sqrt(key)) / (2 * a)
            x2 = (-b - math.sqrt(key)) / (2 * a)
        if key == 0:
            x1 = -b / (2 * a)
            x2 = x1
        if key < 0:
            return None
        return (x1, x2)
    # 线性方程情况
    else:
        x = -(c / b)
        return (x,)


def rank(n, N):
    import itertools
    a1 = list(range(1, N))
    list_2 = []
    for i in itertools.product(a1, repeat=n):
        if sum(i[0:n]) == N:
            list_2.append(i)
    return list_2


# 将列表元素求和的方法
def sumList(someList):
    num = 0
    for i in someList:
        num += i
    return num
