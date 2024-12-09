class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.key if current else None

    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.key if current else None

bst = BinarySearchTree()
grades = [85, 70, 95, 60, 75, 90, 100]

for grade in grades:
    bst.insert(grade)

min_grade = bst.find_min()
max_grade = bst.find_max()

print(f"Nota mínima: {min_grade}")
print(f"Nota máxima: {max_grade}")
