from link_node import DoubleNode


class DoubleLinkList:
    """双向环形链表，可以用一个头节点的方式做，也可以用头节点，尾节点两个节点做"""

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
        elif self.head.next == self.head.pre:
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
        """travel() 遍历整个链表, 遍历可以正向遍历，也可以反向遍历"""
        if self.is_empty():
            return

        # 只有一个节点
        elif self.head.next == self.head.pre:
            print(self.head.item)
        else:
            tmp_node = self.head
            while tmp_node.next != self.head:
                print(tmp_node.item, end=" ")
                tmp_node = tmp_node.next
            # 最后一个节点没打印，这里补充打印一下
            print(tmp_node.item)
            print("")

    def append(self, item):
        """ append(item) 链表尾部添加元素"""
        node = DoubleNode(item)
        # 空节点的时候
        if self.is_empty():
            self.head = node
            # 自己指向自己
            self.head.next = self.head
            self.head.pre = self.head
            # print(self.head.next.item)

        # 单节点的时候
        elif self.head.next == self.head:
            self.head.next = node
            self.head.pre = node
            # print(self.head.next.item)
            node.next = self.head
            node.pre = self.head

        else:
            self.head.pre.next = node
            node.pre = self.head.pre
            node.next = self.head
            self.head.pre = node

    def add(self, item):
        """add(item) 链表头部添加元素"""
        node = DoubleNode(item)
        if self.is_empty():
            self.head = node
            # 自己指向自己
            self.head.next = self.head
            return

        elif self.head.next == self.head:
            self.head.pre = node
            self.head.next = node
            node.pre = self.head
            node.next = self.head

        else:
            node.next = self.head
            node.pre = self.head.pre
            self.head.pre.next = node
            self.head.pre = node
            self.head = node

    def insert(self, pos, item):
        """insert(pos, item) 指定位置添加元素"""
        node = DoubleNode(item)
        if pos <= 1:
            self.add(node)
        elif pos >= self.length():
            self.append(node)
        else:
            count = 1
            cur_node = self.head

            while cur_node.next != self.head:
                if count == pos:
                    break
                cur_node = cur_node.next
                count += 1

            node.pre = cur_node.pre
            node.next = cur_node
            cur_node.pre.next = node
            cur_node.pre = node

    def search(self, item):
        """search(item) 查找节点是否存在"""
        if self.is_empty():
            return -1
        # 只有一个节点的时候
        elif self.head.next == self.head.pre:
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
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
            if cur_node.item == item:
                flag = True
                break
        if flag:
            cur_node.pre.next = cur_node.next
            cur_node.next.pre = cur_node.pre

        else:
            # 循环的最后一个节点还没找到，应该在判断一下最后一个节点
            if cur_node.item == item:
                flag = True
                cur_node.pre.next = self.head
                self.head.pre = cur_node.pre
        return flag

    def clear(self):
        """清空链表"""
        if self.is_empty():
            return
        elif self.length() == 1:
            self.head = None
            self.head.pre = None
            self.head.next = None

        else:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
                cur_node.pre.next = None
                cur_node.pre = None

            cur_node.next = None
            cur_node.pre = None
            self.head.pre = None
            self.head = None


if __name__ == '__main__':
    forward_link = DoubleLinkList(1, 2, 3)
    forward_link.travel()
    forward_link.add(0)
    forward_link.travel()
    print(forward_link.length())
    print(forward_link.search(2))
    forward_link.insert(2, 9)
    forward_link.travel()
    forward_link.remove(9)
    forward_link.travel()
    forward_link.clear()
    print('------------------------')
    forward_link.travel()
    print("------------------------")

