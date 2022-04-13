from public import separatedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        cur_node = head = ListNode(None)

        i = l1
        j = l2

        while True:

            if not i:
                cur_node.next = j
                break

            if not j:
                cur_node.next = i
                break

            if i.val <= j.val:
                cur_node.next = i
                i = i.next

            else:
                cur_node.next = j
                j = j.next

            cur_node = cur_node.next

        return head.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            (l1, l2) = (l2, l1) if l2.val < l1.val else (l1, l2)
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2


if __name__ == '__main__':
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 7, 10]

    listnode1 = separatedList.SinglyList(l1)
    listnode2 = separatedList.SinglyList(l2)

    listnode1.show_singly_list()
    listnode2.show_singly_list()

    solution = Solution()
    node = solution.mergeTwoLists(listnode1.head, listnode2.head)

    while node:
        print(node.val, end='->')
        node = node.next
