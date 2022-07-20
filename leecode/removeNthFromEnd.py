class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if head.next is None:
            return

        if head.next.next is None:

            if n == 1:
                head.next = None
                return head
            if n == 2:
                return head.next

        cur_node = head.next
        n_node = head

        pre_node = None

        while cur_node.next:

            pre_node = n_node
            n_node = cur_node

            for _ in range(1, n):

                cur_node = cur_node.next

        pre_node.next = n_node.next

        return head


if __name__ == "__main__":

    s = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    s.removeNthFromEnd(head, 2)
