class Node:
    """单向链表的节点类"""
    def __init__(self, item):
        """要插入的item数据"""
        self.item = item
        self.next = None
        # 默认下个节点为空


if __name__ == '__main__':
    node = Node(5)
    print(node.item, node.next)
