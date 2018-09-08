# 用数组模拟一个栈，我们规定，栈是吃了吐，尾部添加，尾部删除


class Stack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.push(item)

    def push(self, item):
        """push(item) 添加一个新的元素item到栈顶"""
        self.stack.append(item)

    def pop(self):
        """pop() 弹出栈顶元素"""
        return self.stack.pop()

    def peek(self):
        """peek() 返回栈顶元素"""
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) <= 0

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack(1, 2, 3, 4, 5)
    print(stack.peek())
    print(stack.size())
    print(stack.is_empty())
    stack.pop()
    print(stack.peek())
