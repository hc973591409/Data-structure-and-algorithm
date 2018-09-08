import quick_sort


def bin_search(alist, item):
    """搜索是在一个项目集合中找到一个特定项目的算法过程。搜索通常的答案是真的或假的，因为该项目是否存在。
    搜索的几种常见方法：顺序查找、二分法查找、二叉树查找、哈希查找 最优时间复杂度：O(1) 最坏时间复杂度：O(log n)"""
    n = len(alist)
    mid_index = n // 2
    if n <= 0:
        return False

    else:
        if alist[mid_index] == item:
            return True
        elif alist[mid_index] > item:
            return bin_search(alist[:mid_index], item)
        else:
            return bin_search(alist[mid_index+1:], item)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort.quick_sort(li, 0, len(li)-1)
    print("----------------------")
    print(bin_search(li, 54))
    print(li)
