from link_node import Node


class CycleForwardLink:
    """单向链表"""

    def __init__(self, *args):
        """插入个链表，如果有节点就插入，没有就让头节点为空"""
        self.head = None
        for item in args:
            self.append(item)

    def is_empty(self):
        """is_empty() 链表是否为空"""
        if not self.head:
            return True
        else:
            return False

    def length(self):
        """length() 链表长度"""
        if not self.head:
            return 0

        # 只有一个节点的时候，单向循环链表的next指向自己
        elif self.head.next == self.head:
            return 1

        # 循环到next指向头节点的时候
        else:
            count = 0
            tmp_node = self.head
            while tmp_node.next != self.head:
                tmp_node = tmp_node.next
                count += 1
            # 最后一个节点没进入循环，返回的时候应该增加1返回
            return count+1

    def travel(self):
        """travel() 遍历整个链表"""
        if self.is_empty():
            return
        tmp_node = self.head
        while tmp_node.next != self.head:
            print(tmp_node.item, end=" ")
            tmp_node = tmp_node.next
        # 最后一个节点没打印，这里补充打印一下
        print(tmp_node.item)
        print("")

    def append(self, item):
        """ append(item) 链表尾部添加元素"""
        node = Node(item)
        # 空节点的时候
        if self.is_empty():
            self.head = node
            # 自己指向自己
            self.head.next = self.head

        # 单节点的时候
        elif self.head.next == self.head:
            self.head.next = node
            node.next = self.head
        else:
            tmp_node = self.head
            while tmp_node.next != self.head:
                tmp_node = tmp_node.next

            tmp_node.next = node
            node.next = self.head

    def add(self, item):
        """add(item) 链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.head.next = self.head
            return

        tmp_node = self.head
        while tmp_node.next != self.head:
            tmp_node = tmp_node.next

        node.next = self.head
        tmp_node.next = node
        self.head = node

    def insert(self, pos, item):
        """insert(pos, item) 指定位置添加元素"""
        node = Node(item)
        if pos <= 1:
            self.add(node)
        elif pos >= self.length():
            self.append(node)
        else:
            count = 1
            pre_node = self.head
            next_node = self.head

            while next_node.next != self.head:
                pre_node = next_node
                next_node = next_node.next
                count += 1
                if count == pos:
                    break

            pre_node.next = node
            node.next = next_node

    def search(self, item):
        """search(item) 查找节点是否存在"""
        if self.is_empty():
            return -1
        # 只有一个节点的时候
        elif self.head.next == self.head:
            if self.head.item == item:
                return 0
        else:
            tmp_node = self.head
            index = 0
            while tmp_node.next != self.head:
                if tmp_node.item == item:
                    return index
                index += 1
                tmp_node = tmp_node.next

            if tmp_node.item == item:
                index += 1
                return index
            return -1

    def remove(self, item):
        """# remove(item) 删除节点 成功返回True 否则false"""
        if self.is_empty():
            return False

        if self.length() == 1:
            if self.head.item == item:
                self.head = None
                self.head.next = None
                return True
            else:
                return False

        flag = False
        pre_node = self.head
        next_node = self.head
        while next_node.next != self.head:
            pre_node = next_node
            next_node = next_node.next
            if next_node.item == item:
                flag = True
                break

        if flag:
            pre_node.next = next_node.next

        else:
            # 循环的最后一个节点还没找到，应该在判断一下最后一个节点
            if next_node.item == item:
                flag = True
                pre_node.next = self.head

        return flag

    def clear(self):
        """清空链表"""
        if self.is_empty():
            return
        elif self.length() == 1:
            self.head = None

        pre_node = self.head
        next_node = self.head

        while next_node.next != self.head:
            pre_node = next_node
            pre_node.next = None
            next_node = next_node.next

        next_node.next = None

        self.head = None
        self.head.next = None


if __name__ == '__main__':
    forward_link = CycleForwardLink(1, 2, 3)
    forward_link.travel()
    forward_link.add(0)
    forward_link.travel()
    print(forward_link.length())
    print(forward_link.search(7))
    forward_link.insert(2, 9)
    forward_link.travel()
    forward_link.remove(9)
    forward_link.travel()
    forward_link.clear()
    print('------------------------')
    forward_link.travel()
    print("------------------------")

