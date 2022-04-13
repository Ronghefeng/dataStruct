import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        length = 0
        cur_node = copy.deepcopy(root)
        while cur_node:
            length += 1
            cur_node = cur_node.next

        count, remainder = divmod(length, k)
        result = []

        # 保证间隔数都为 k，不够则添加 None
        for i in range(k):
            head = cur_node = ListNode(None)

            # count < remainder 从前往后在每个分组中只增加一个长度
            for j in range(count + (i < remainder)):
                # 上一节点指针
                tmp = cur_node
                cur_node.next = ListNode(root.val)
                cur_node = ListNode(root.val)
                tmp.next = cur_node
                # cur_node.next = cur_node = ListNode(root.val)

                if root.next:
                    root = root.next

            result.append(head.next)
        return result

    def output(self, results):
        i = 1
        for r in results:
            print('第 %s 个链表' % i)
            while r:
                print(r.val, end='->')
                r = r.next
                i += 1
            print('Null')


# class Solution(object):
#     def splitListToParts(self, root, k):
#         cur = root
#         for N in range(1001):
#             if not cur: break
#             cur = cur.next
#         width, remainder = divmod(N, k)
#
#         ans = []
#         cur = root
#         for i in range(k):
#             head = write = ListNode(None)
#             for j in range(width + (i < remainder)):
#                 write.next = write = ListNode(cur.val)
#                 if cur: cur = cur.next
#             ans.append(head.next)
#         return ans
#
#     def output(self, results):
#         i = 1
#         for r in results:
#             print('第 %s 个链表' % i)
#             while r:
#                 print(r.val, end='->')
#                 r = r.next
#                 i += 1
#             print('Null')


class SinglyList:
    def __init__(self, data):
        if not data:
            self.head = None
            return

        self.head = ListNode(data[0])
        p = self.head

        for d in data[1:]:
            node = ListNode(d)
            p.next = node
            p = p.next

    def show_singly_list(self):
        p = self.head
        while p:
            print(str(p.val) + '->', end='')
            p = p.next
        print('Null')

if __name__ == '__main__':
    root = [1,2,3,4,5,6,7,8,9,10]
    k = input('Please input the value of k: ')
    singly_list = SinglyList(root)
    singly_list.show_singly_list()
    solution = Solution()
    results = solution.splitListToParts(singly_list.head, int(k))
    solution.output(results)

