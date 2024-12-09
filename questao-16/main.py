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

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_larger_node = self._find_min(node.right)
                node.key = min_larger_node.key
                node.right = self._remove(node.right, min_larger_node.key)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

bst = BinarySearchTree()
codes = [45, 25, 65, 20, 30, 60, 70]

for code in codes:
    bst.insert(code)

print("Árvore em ordem crescente:")
bst.inorder_traversal(bst.root)
print("\nRemovendo 20 (nó folha):")
bst.remove(20)
bst.inorder_traversal(bst.root)
print("\nRemovendo 25 (nó com um filho):")
bst.remove(25)
bst.inorder_traversal(bst.root)
print("\nRemovendo 45 (nó com dois filhos):")
bst.remove(45)
bst.inorder_traversal(bst.root)
