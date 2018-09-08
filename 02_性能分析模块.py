import timeit

"""导入性能分析模块"""


def test1():
    list_1 = []
    for i in range(1000):
        list_1 = list_1 + [i]


def test2():
    """列表的appen方法"""
    list_1 = []
    for i in range(1000):
        list_1.append(i)


def test3():
    """列表生成式"""
    list_1 = [i for i in range(1000)]


def test4():
    """通过列表转换"""
    list_1 = list(range(1000))


t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "seconds")
# concat  1.471402666 seconds
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("concat ", t1.timeit(number=1000), "seconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("concat ", t1.timeit(number=1000), "seconds")
t4 = timeit.Timer("test4()", "from __main__ import test")
print("concat ", t1.timeit(number=1000), "seconds")