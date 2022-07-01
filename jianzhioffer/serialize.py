import collections
from lib2to3.pytree import Node
from treeNode import TreeNode


class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return []

        result = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()

            if node is None:
                result.append(None)
            else:
                result.append(node.val)

            if node is not None:
                queue.append(node.left)

            if node is not None:
                queue.append(node.right)
        while result[-1] is None:
            result = result[:-1]
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        queue = collections.deque(data)

        val = queue.popleft()

        root = TreeNode(val)

        level_queue = collections.deque([root])

        while queue:
            cur = level_queue.popleft()

            left_val = queue.popleft()

            left = None
            right = None

            if left_val is not None:
                left = TreeNode(left_val)

            if queue:
                right_val = queue.popleft()
                if right_val is not None:
                    right = TreeNode(right_val)

            cur.left = left
            cur.right = right

            if left:
                level_queue.append(left)
            if right:
                level_queue.append(right)

        return root


class Codec1:
    def serialize(self, root):
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        if data == "[]":
            return
        vals, i = data[1:-1].split(","), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == "__main__":

    c = Codec()

    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.right.left = TreeNode(4)
    tree1.right.right = TreeNode(5)

    data = c.serialize(tree1)

    print(data)

    tree2 = c.deserialize(data)

    print(c.serialize(tree2))
