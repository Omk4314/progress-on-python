class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.key})"


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_recursive(self.root, key)
        return deleted

    def _delete_recursive(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted
        else:
            if node.left is None and node.right is None:
                return None, True
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right, _ = self._delete_recursive(node.right, successor.key)
            return node, True

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    tree = BST()

    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        tree.insert(k)
    print("Inorder after inserts:", tree.inorder())

    print("Search 40:", tree.search(40))
    print("Search 100:", tree.search(100))

    tree.delete(20)
    print("Delete 20 (leaf):", tree.inorder())

    tree.delete(30)
    print("Delete 30 (one child):", tree.inorder())

    tree.delete(50)
    print("Delete 50 (two children):", tree.inorder())