class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class FileSystem:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name):
        if self.root is None:
            self.root = Node(parent_name)
            self.root.left = Node(child_name)
            return

        parent = self._find(self.root, parent_name)
        if parent:
            if parent.left is None:
                parent.left = Node(child_name)
            else:
                current = parent.left
                while current.right:
                    current = current.right
                current.right = Node(child_name)

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found:
            return found
        return self._find(node.right, name)

    def show(self, node=None, prefix="", is_last=True):
        if node is None:
            node = self.root
        if node is None:
            return

        branch = "`-- " if is_last else "|-- "
        print(prefix + branch + node.name)

        if node.left:
            child_prefix = prefix + ("    " if is_last else "|   ")
            self._show_siblings(node.left, child_prefix)

    def _show_siblings(self, node, prefix):
        while node:
            is_last = node.right is None
            self.show(node, prefix, is_last)
            node = node.right


fs = FileSystem()
fs.insert("home", "auto.sh")
fs.insert("home", "Desktop")
fs.insert("home", "Documents")
fs.insert("home", "Downloads")
fs.insert("home", "Music")
fs.insert("home", "Pictures")
fs.insert("home", "Public")
fs.insert("home", "snap")
fs.insert("snap", "snapd-desktop-integration")
fs.insert("snapd-desktop-integration", "49")
fs.insert("snapd-desktop-integration", "common")
fs.insert("snapd-desktop-integration", "current -> 49")
fs.insert("home", "Templates")
fs.insert("home", "Videos")
fs.show()