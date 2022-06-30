from typing import List
from treeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            # 根据同步执行顺序实现回溯
            recur(root.left, tar)
            recur(root.right, tar)
            # 删除不符合条件路径
            path.pop()

        recur(root, target)
        return res


if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right = TreeNode(8)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.left = TreeNode(5)
    root1.right.right.right = TreeNode(1)

    for postorder, result in [[root1, [[5, 4, 11, 2], [5, 8, 4, 5]]]]:
        print("计算结果: %s, 预期结果: %s" % (s.pathSum(postorder, 22), result))
