
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        if head.val == val:
            return head.next

        pre_node, cur_node = head, head.next

        while cur_node != None:

            if cur_node.val == val:
                pre_node.next = cur_node.next
                return head

            pre_node = cur_node
            cur_node = cur_node.next

        return head


if __name__ == '__main__':
    n = input('Please input the x and n: ')
    solution = Solution()
    print(solution.deleteNode(int(n)))