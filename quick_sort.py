def quick_sort(alist, start, end):
    """快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所
    有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，
    以此达到整个数据变成有序序列。  最坏时间复杂度为O(N^2),最优时间复杂度为O(log n)"""

    # 递归出口
    if start >= end:
        return

    # 设定基准元素
    mid = alist[start]

    left_flag = start
    right_flag = end

    while left_flag < right_flag:
        while alist[right_flag] >= mid and left_flag < right_flag:
            right_flag -= 1

        alist[left_flag] = alist[right_flag]

        while alist[left_flag] < mid and left_flag < right_flag:
            left_flag += 1

        alist[right_flag] = alist[left_flag]

    alist[left_flag] = mid
    # 右边
    quick_sort(alist, start, left_flag-1)
    quick_sort(alist, right_flag+1, end)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(li, 0, len(li)-1)
    print(li)
