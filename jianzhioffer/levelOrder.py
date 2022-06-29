import collections
from typing import List
from treeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 层序遍历，从左到右，输出到一行

        if root is None:
            return []

        node_list = [root]
        result = []

        while True:

            if len(node_list) == 0:
                break

            level_list = []

            for node in node_list:

                result.append(node.val)

                if node.left is not None:
                    level_list.append(node.left)
                if node.right is not None:
                    level_list.append(node.right)

            node_list = level_list

        return result

    def levelOrder1(self, root: TreeNode) -> List[int]:
        # 层序遍历，从左到右，输出到一行

        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def levelOrder2(self, root: TreeNode) -> List[int]:
        # 层序遍历，从左到右，一层一行
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            nodes = list(queue)
            queue.clear()
            tmp = []
            for node_ in nodes:
                tmp.append(node_.val)
                if node_.left:
                    queue.append(node_.left)
                if node_.right:
                    queue.append(node_.right)
            res.append(tmp)
        return res

    def levelOrder3(self, root: TreeNode) -> List[int]:
        # 层序遍历，从左到右，一层一行
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node_ = queue.popleft()
                tmp.append(node_.val)
                if node_.left:
                    queue.append(node_.left)
                if node_.right:
                    queue.append(node_.right)
            res.append(tmp)
        return res

    def levelOrder4(self, root: TreeNode) -> List[int]:
        # 层序遍历，锯齿形输出
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        level = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node_ = queue.popleft()
                if node_ is not None:
                    if level % 2 == 0:
                        tmp.insert(0, node_.val)
                    else:
                        tmp.append(node_.val)
                    if node_.left:
                        queue.append(node_.left)
                    if node_.right:
                        queue.append(node_.right)
            level += 1
            res.append(tmp)
        return res

    def levelOrder5(self, root: TreeNode) -> List[List[int]]:
        # 层序遍历，锯齿形输出
        if not root:
            return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)  # 偶数层 -> 队列头部
                else:
                    tmp.append(node.val)  # 奇数层 -> 队列尾部
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res


if __name__ == "__main__":

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    print("root 结果：", s.levelOrder4(root))
    print("root1 结果：", s.levelOrder4(root1))
