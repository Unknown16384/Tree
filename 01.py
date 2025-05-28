class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def _insert(self, cur_node, value):
        if not cur_node: return Node(value)
        elif value < cur_node.value: cur_node.left = self._insert(cur_node.left, value)
        else: cur_node.right = self._insert(cur_node.right, value)
        return cur_node
    def _search(self, root, value):
        if not root: return False
        elif root.value < value: return self._search(root.right, value)
        elif root.value > value: return self._search(root.left, value)
        return True
    def insert(self, value):
        self.root = self._insert(self.root, value)
    def search(self, value):
        return self._search(self.root, value)

'''а что конкретно должен возвращать метод search у бинарного дерева? на видео уроках про это не слова :) реализовал просто True/False'''