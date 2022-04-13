# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = preorder[0]

        for i in range(len(inorder)):
            if inorder[i] == root:
                break

        left = self.buildTree(preorder[1: 1 + i], inorder[:i])
        right = self.buildTree(preorder[1+ i:], inorder[i + 1:])

        node = TreeNode(root)
        node.left = left
        node.right = right

        return node


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def construct_tree(pre_order, inroder):

    if len(pre_order) == 0 or len(inroder) == 0:
        return None
    # 前序遍历的第一个结点一定是根结点
    root_data = pre_order[0]
    for i in range(0, len(inroder)):
        if inroder[i] == root_data:
            break
    # 递归构造左子树和右子树
    left = construct_tree(pre_order[1: 1 + i], inroder[:i])
    right = construct_tree(pre_order[1 + i:], inroder[i + 1:])
    return Node(root_data, left, right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            node.right = recur(i + 1 - left + root, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    # node = construct_tree(preorder, inorder)
    # print(node.data)
    solution = Solution()
    result = solution.buildTree(preorder, inorder)
    print(result.val)
