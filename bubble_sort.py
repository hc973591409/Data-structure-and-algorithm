def bubble_sort(alist):
    """冒泡排序（英语：Bubble
    Sort）是一种简单的排序算法。它重复地遍历要排序的数列，
    一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没
    有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢
    慢“浮”到数列的顶端"""
    # 默认没有交换过，如果一次循环没有发生交换，那么就是有序的
    flag = False
    n = len(alist)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                flag = True

        if not flag:
            return


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)
