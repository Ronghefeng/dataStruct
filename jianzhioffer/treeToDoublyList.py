from treeNode import TreeNode


class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:

        if not root:
            return

        result = []

        def traverse(node):

            if node:
                traverse(node.left)
                result.append(node)
                traverse(node.right)

        traverse(root)

        cur = head = result[0]

        for node in result[1:]:

            cur.right = node
            node.left = cur
            cur = node

        cur.right = head
        head.left = cur

        return head

    def treeToDoublyList1(self, root: TreeNode) -> TreeNode:

        if not root:
            return

        self.pre = None

        def traverse(node):

            if node:
                traverse(node.left)
                if self.pre:
                    self.pre.right = node
                    node.left = self.pre
                else:
                    self.head = node
                self.pre = node
                traverse(node.right)

        traverse(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head


if __name__ == "__main__":
    s = Solution()

    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(5)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)

    new_list = s.treeToDoublyList(tree1)
