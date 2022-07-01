from treeNode import TreeNode


def preorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

    traverse(root)
    return result


def inorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return result


def postorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

    traverse(root)
    return result


if __name__ == "__main__":

    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(5)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)

    print("先序遍历：", preorder_traversal(tree1))
    print("中序遍历：", inorder_traversal(tree1))
    print("后序遍历：", postorder_traversal(tree1))
