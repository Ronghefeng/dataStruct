class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def gener_tree(self, node_list: list):

        length = len(node_list)
        i = 0
