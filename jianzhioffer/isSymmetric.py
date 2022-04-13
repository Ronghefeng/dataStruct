# Definition for a binary tree node.
from turtle import left, right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        if root.right == root.left:
            return True

        if self.isSymmetric(root.left) and self.isSymmetric(root.right):
            return True

        return False
