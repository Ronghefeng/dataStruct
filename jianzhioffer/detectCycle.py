# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        node_sets = set()

        cur_node = head

        while cur_node:

            if cur_node in node_sets:
                return cur_node

            node_sets.add(cur_node)
            cur_node = cur_node.next

        return None
