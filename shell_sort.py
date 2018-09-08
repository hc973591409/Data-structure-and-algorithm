def shell_sort(alist):
    """希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，
    是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排
    序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把
    记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随
    着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文
    件恰被分成一组，算法便终止, 时间复杂度随gap的量而定"""
    n = len(alist)
    gap = n//2
    while gap >= 1:
        for i in range(0, n, gap):
            if (i-gap) >= 0 and alist[i] < alist[i-gap]:
                alist[i], alist[i-gap] = alist[i-gap], alist[i]
        gap //= 2


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(li)
    print(li)
