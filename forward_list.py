from link_node import Node


class ForwardLink:
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
        elif not self.head:
            return 1
        else:
            count = 0
            tmp_node = self.head
            while tmp_node:
                tmp_node = tmp_node.next
                count += 1
            return count

    def travel(self):
        """travel() 遍历整个链表"""
        if self.is_empty():
            return
        tmp_node = self.head
        while tmp_node:
            print(tmp_node.item, end=" ")
            tmp_node = tmp_node.next
        print("")

    def append(self, item):
        """ append(item) 链表尾部添加元素"""
        node = Node(item)
        # 空节点的时候
        if self.is_empty():
            self.head = node

        # 单节点的时候
        elif not self.head.next:
            self.head.next = node
        else:
            tmp_node = self.head
            while tmp_node.next:
                tmp_node = tmp_node.next

            tmp_node.next = node

    def add(self, item):
        """add(item) 链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.head = node
            return
        node.next = self.head
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

            while next_node:
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
        else:
            tmp_node = self.head
            index = 0
            while tmp_node:
                if tmp_node.item == item:
                    return index
                index += 1
                tmp_node = tmp_node.next

            return -1

    def remove(self, item):
        """# remove(item) 删除节点 成功返回True 否则false"""
        if self.is_empty():
            return False

        if self.length() == 1:
            if self.head.item == item:
                self.head = None
                return True
            else:
                return False
        flag = False
        pre_node = self.head
        next_node = self.head
        while next_node:
            pre_node = next_node
            next_node = next_node.next
            if next_node.item == item:
                flag = True
                break
        if flag:
            pre_node.next = next_node.next
        return flag

    def clear(self):
        """清空链表"""
        if self.is_empty():
            return
        elif self.length() == 1:
            self.head = None

        pre_node = self.head
        next_node = self.head
        while next_node:
            pre_node = next_node
            pre_node.next = None
            next_node = next_node.next

        self.head = None


if __name__ == '__main__':
    forward_link = ForwardLink(1, 2, 3)
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

