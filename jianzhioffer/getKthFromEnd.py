from public import separatedList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        linknode = head

        length = 0
        while linknode:
            length += 1
            linknode = linknode.next

        if k > length:
            return ListNode(None)

        i = 0
        while i < (length - k):
            i += 1
            head = head.next

        return head


if __name__ == '__main__':
    nums = [0,7,1,4,8,5,6,6,8,3,8,5,1,9,4,1]
    listnode = separatedList.SinglyList(nums)
    listnode.show_singly_list()
    solution = Solution()
    print(solution.getKthFromEnd(listnode.head, 13))