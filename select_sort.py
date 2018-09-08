def select_sort(alist):
    """选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩
    余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直
    到所有元素均排序完毕。  最坏时间复杂度为O(N^2)"""

    n = len(alist)
    for i in range(n-1, 0, -1):
        max_index = 0
        for j in range(0, i):
            if alist[j] > alist[max_index]:
                max_index = j
        alist[i], alist[max_index] = alist[max_index], alist[i]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select_sort(li)
    print(li)
