
class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item):
        # 空节点的时候
        node = Node(item)
        if not self.root:
            self.root = node

        else:
            queue_list = [self.root]
            while queue_list:
                # 弹出一个元素
                cur_node = queue_list.pop(0)
                if cur_node.left is None:
                    cur_node.left = node
                    return
                elif cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    queue_list.append(cur_node.left)
                    queue_list.append(cur_node.right)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.item)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

    def pre_deep_travel(self, cur_node):
        """先序：深度优先遍历，根左右"""
        if cur_node is None:
            return

        print(cur_node.item)
        self.pre_deep_travel(cur_node.left)
        self.pre_deep_travel(cur_node.right)

    def mid_deep_travel(self, cur_node):
        """中序：深度优先遍历，左，中，右"""
        if cur_node is None:
            return
        self.mid_deep_travel(cur_node.left)
        print(cur_node.item)
        self.mid_deep_travel(cur_node.right)

    def post_deep_travel(self, cur_node):
        """后序：深度优先遍历，左，右，中"""
        if cur_node is None:
            return
        self.post_deep_travel(cur_node.left)
        self.post_deep_travel(cur_node.right)
        print(cur_node.item)


if __name__ == '__main__':
    binary_tree = BinaryTree()
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(6)
    # binary_tree.breadth_travel()
    # binary_tree.pre_deep_travel(binary_tree.root)
    # binary_tree.mid_deep_travel(binary_tree.root)
    binary_tree.post_deep_travel(binary_tree.root)