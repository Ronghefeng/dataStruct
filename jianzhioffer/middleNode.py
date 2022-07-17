# Definition for singly-linked list.
from math import ceil


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 遍历两次

        tmp_node = head

        length = 0

        while tmp_node:
            length += 1
            tmp_node = tmp_node.next

        target_index = length // 2

        i = 0

        target_node = head

        while i < target_index:

            i += 1

            target_node = target_node.next

        return target_node

    def middleNode2(self, head: ListNode) -> ListNode:
        # 遍历一次+数组存储

        tmp_node = head
        nodes = []
        length = 0
        while tmp_node:
            length += 1
            nodes.append(tmp_node)

            tmp_node = tmp_node.next

        index = length // 2

        return nodes[index]

    def middleNode3(self, head: ListNode) -> ListNode:
        # 快慢指针

        slow = fast = head

        while fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow
