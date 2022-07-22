from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        cur_node = head

        node_stack = list()

        last = -1

        while cur_node:
            node_stack.append(cur_node)
            last += 1
            cur_node = cur_node.next

        first = 0

        while first <= last:
            if node_stack[first].val != node_stack[last].val:
                return False
            first += 1
            last -= 1
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next or not head.next.next:
            return head

        first = head
        second = tmp_second = head.next

        while first and second:
            if not second.next:
                break

            first.next = second.next
            first = first.next

            second.next = first.next
            second = second.next

        first.next = tmp_second

        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        cur_node = head

        node_list = list()

        while cur_node:
            node_list.append(cur_node)
            cur_node = cur_node.next

        self.sort_node(node_list, 0, len(node_list))

        cur_node = new_head = node_list.pop(0)

        while node_list:
            cur_node.next = node_list.pop(0)
            cur_node = cur_node.next

        cur_node.next = None

        return new_head

    def sort_node(self, node_list, low, high):
        if not node_list:
            return

        if low < high - 1:

            pivot_index = self.find_pivot(node_list, low, high)
            self.sort_node(node_list, low, pivot_index)
            self.sort_node(node_list, pivot_index + 1, high)

    def find_pivot(self, node_list, low, high):

        i = low
        pivot = node_list[low].val

        for j in range(low + 1, high):

            if node_list[j].val <= pivot:
                i += 1
                node_list[i], node_list[j] = node_list[j], node_list[i]

        node_list[low], node_list[i] = node_list[i], node_list[low]

        return i

    def sortList1(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)


if __name__ == "__main__":

    s = Solution()

    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(8)
    # head.next.next.next.next.next = ListNode(6)
    print(s.sortList(head))
