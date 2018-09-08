# Queue() 创建一个空的队列
# enqueue(item) 往队列中添加一个item元素
# dequeue() 从队列头部删除一个元素
# is_empty() 判断一个队列是否为空
# size() 返回队列的大小
# 可以用链表或者列表实现队列


class Queue:
    def __init__(self, *args):
        self.queue = []
        for item in args:
            self.enqueue(item)

    def enqueue(self, item):
        """enqueue(item) 往队列中添加一个item元素,尾部添加"""
        self.queue.append(item)

    def dequeue(self):
        """# dequeue() 从队列头部删除一个元素"""
        del self.queue[0]

    def get(self):
        """# 获取队列前端的元素"""
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) <= 0

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    queue = Queue(1, 2, 3, 4, 5)
    print(queue.get())
    print(queue.is_empty())
    queue.dequeue()
    print(queue.get())
    queue.dequeue()
    print(queue.get())
    print(queue.size())

