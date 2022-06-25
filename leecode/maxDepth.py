# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepthRecursion(self, root: TreeNode):

        left_depth = right_depth = max_depth = 0

        if root is None:
            return 0

        if root.left is None and root.right is None:

            return 1

        if root.left:

            left_depth += 1
            left_depth += self.maxDepthRecursion(root.left)

        if root.right:

            right_depth += 1
            right_depth += self.maxDepthRecursion(root=root.right)

        max_depth = max(left_depth, right_depth)

        return max_depth

    def maxDepth(self, root: TreeNode):

        if root is None:
            return 0

        node_list = [root]

        max_depth = self.count_depth(node_list)

        return max_depth

    def count_depth(self, node_list):

        max_depth = 0

        while True:

            if len(node_list) == 0:
                break

            list_length = len(node_list)

            for i in range(list_length):

                if node_list[i].left is None and node_list[i].right is None:
                    continue

                if node_list[i].left:
                    node_list.append(node_list[i].left)

                if node_list[i].right:
                    node_list.append(node_list[i].right)

            node_list = node_list[list_length:]

            max_depth += 1

        return max_depth


if __name__ == "__main__":

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)

    root.right.right = TreeNode(5)

    s = Solution()

    max_depth1 = s.maxDepth(root)

    max_depth2 = s.maxDepthRecursion(root)

    print(max_depth1, max_depth2)
