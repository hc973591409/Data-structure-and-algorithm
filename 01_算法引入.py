import time


def calc_1():
    """# 计算a+b+c == 1000 且 a^2+b^2=c^2"""
    time_start = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    print("%s + %s + %s = 1000" % (a, b, c))

    time_end = time.time()
    print("程序共耗时%s s" % (time_end-time_start))
    # 程序共耗时148.1957812309265s    时间复杂度O(N^3)


def calc_2():
    """修改程序，优化算法"""
    time_start = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print("%s + %s + %s = 1000" % (a, b, c))

    time_end = time.time()
    print("程序共耗时%.2f s" % (time_end-time_start))
    # 程序共耗时程序共耗时1.12 s     时间复杂度O(N^2)


if __name__ == '__main__':
    calc_2()
