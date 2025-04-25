class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, node, target):
        if node is None:
            return None
        if node.data == target:
            return True
        elif node.data > target:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    def insert(self, node, data):
        if node is None:
            return TreeNode(data)
        else:
            if node.data > data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
        return node

    def delete(self, node, data):
        if not node:
            return None
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            node.data = self.get_min(node.right).data
            node.right = self.delete(node.right, node.data)
        return node

    def inorder_traversal(self, node):
        if node is None:
            return None
        self.inorder_traversal(node.left)
        print(node.data, end=", ")
        self.inorder_traversal(node.right)

    def get_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

if __name__ == '__main__':
    root = TreeNode(10)
    node8 = TreeNode(8)
    node12 = TreeNode(12)
    node6 = TreeNode(6)
    node14 = TreeNode(14)
    node4 = TreeNode(4)
    node16 = TreeNode(16)

    root.left, root.right = node6, node14
    node6.left, node6.right = node4, node8
    node14.right, node14.left = node16, node12
    # root.insert(root, 11)
    root.inorder_traversal(root)
    print()
    root.delete(root, 15)
    root.inorder_traversal(root)






