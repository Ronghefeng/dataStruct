# Definition for singly-linked list.
from public.separatedList import SinglyList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        result = []
        while head.val:
            result.insert(0, head.val)
            head = head.next
        return result


if __name__ == '__main__':
    data = []
    singly_list = SinglyList(data)
    head = singly_list.head
    solution = Solution()
    result = solution.reversePrint(head)
    print(result)
