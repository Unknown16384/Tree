class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(BinaryTree):
    def _insert(self, cur_node, value):
        if not cur_node: return AVLNode(value)
        elif value < cur_node.value: cur_node.left = self._insert(cur_node.left, value)
        else: cur_node.right = self._insert(cur_node.right, value)
        cur_node.height = 1 + max(self.height(cur_node.left), self.height(cur_node.right))
        balance = self.balance(cur_node)
        if balance > 1 and value < cur_node.left.value:
            return self.right_rotate(cur_node)
        if balance < -1 and value > cur_node.right.value:
            return self.left_rotate(cur_node)
        if balance > 1 and value > cur_node.left.value:
            cur_node.left = self.left_rotate(cur_node.left)
            return self.right_rotate(cur_node)
        if balance < -1 and value < cur_node.right.value:
            cur_node.right = self.right_rotate(cur_node.right)
            return self.left_rotate(cur_node)
        return cur_node
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    def height(self, cur_node):
        if not cur_node: return 0
        return cur_node.height
    def balance(self, cur_node):
        if not cur_node: return 0
        return self.height(cur_node.left) - self.height(cur_node.right)