import os, sys

# 导入上级同级目录文件
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from public import separatedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        reverse_list = []

        while head:
            reverse_list.append(head.val)
            head = head.next

        cur_node = reverse_head = ListNode(reverse_list.pop())
        for i in range(len(reverse_list))[::-1]:

            node = ListNode(reverse_list.pop())
            cur_node.next = node
            cur_node = node

        return reverse_head

    def reverseList2(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        node = self.reverseList2(head.next)
        head.next.next = head
        head.next = None

        return node

    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = ListNode(None), head

        while pre:
            node = pre.next
            pre.next = cur
            cur = pre
            pre = node

        return cur

    def reverseList3(self, head: ListNode) -> ListNode:

        if not head:
            return None

        if not head.next:
            return head
        i, j = head, head.next
        i.next = None
        while j:
            next_node = j.next
            j.next = i
            i = j
            j = next_node
        return i

    def reverseList3(self, head: ListNode) -> ListNode:


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    listnode = separatedList.SinglyList(nums)
    listnode.show_singly_list()
    solution = Solution()
    node = solution.reverseList4(listnode.head)
    while node:
        print(node.val, end="->")
        node = node.next
