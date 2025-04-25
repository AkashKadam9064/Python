class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder_traversal(self, node):
        # root-->left-->right
        if node is None:
            return
        print(node.data, end=", ")
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        # left-->root-->right
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.data, end=", ")
        self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        # left-->right-->root
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data, end=", ")

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

    print(root.preorder_traversal(root))
    print(root.inorder_traversal(root))
    print(root.postorder_traversal(root))

