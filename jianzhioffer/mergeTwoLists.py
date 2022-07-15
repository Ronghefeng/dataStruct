import os, sys

# 导入上级同级目录文件
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from typing import Optional
from public import separatedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists1(self, list1: ListNode, list2: ListNode) -> ListNode:

        if not list1:
            return list2
        if not list2:
            return list1

        cur_node = head = ListNode(None)

        i = list1
        j = list2

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

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 and list2:
            (list1, list2) = (list2, list1) if list2.val < list1.val else (list1, list2)
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1 or list2

    def mergeTwoLists2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not list1 and not list2:
            return None

        if not list1:
            return list2

        if not list2:
            return list1

        i = list1
        j = list2

        if i.val > j.val:
            head = j
            i, j = j, i

        else:
            head = i

        while i and j:

            if i.val <= j.val:

                if i.next:

                    if i.next.val <= j.val:
                        i = i.next
                    else:
                        next_node = i.next
                        i.next = j
                        i = j
                        j = next_node

                else:
                    i.next = j
                    break

            else:
                i = i.next

        return head


if __name__ == "__main__":

    list1 = [-6, -2, -1, 0, 3, 6, 7, 9]
    list2 = [-9, -7, -5, -5, -1, 0, 0, 5, 9]
    listnode1 = separatedList.SinglyList(list1)
    listnode2 = separatedList.SinglyList(list2)

    listnode1.show_singly_list()
    listnode2.show_singly_list()

    solution = Solution()
    node = solution.mergeTwoLists2(listnode1.head, listnode2.head)

    while node:
        print(node.val, end="->")
        node = node.next
