class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def get_list(self, head: "Node"):
        cur_head = head

        lists = []

        while cur_head:

            tmp_list = [cur_head.val]

            if cur_head.random is None:
                tmp_list.append(None)
                lists.append(tmp_list)
                cur_head = cur_head.next
                continue

            i = 0
            cur_node = head
            while cur_node:
                if cur_node.val == cur_head.random.val:
                    tmp_list.append(i)
                    lists.append(tmp_list)
                    break
                cur_node = cur_node.next
                i += 1

            cur_head = cur_head.next

        return lists

    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return

        if head.next is None and head.random is None:
            return Node(head.val)

        cur_head = head

        new_head = new_list = Node(head.val)

        lists = []

        while cur_head:

            new_head.next = Node(cur_head.val)
            new_head = new_head.next

            tmp_list = [cur_head.val]

            if cur_head.random is None:
                tmp_list.append(None)
                lists.append(tmp_list)
                cur_head = cur_head.next
                continue

            i = 0
            cur_node = head
            while cur_node:
                if cur_node == cur_head.random:
                    tmp_list.append(i)
                    lists.append(tmp_list)
                    break
                cur_node = cur_node.next
                i += 1

            cur_head = cur_head.next

        new_head_ = new_list = new_list.next

        j = 0

        for _, index in lists:

            if index is None:
                new_head_ = new_head_.next
                j += 1
                continue

            if index > j:
                cur = new_head_

                range_ = (j, len(lists))

            else:
                cur = new_list

                range_ = (0, j + 1)

            for i in range(*range_):

                if i == index:
                    new_head_.random = cur
                    break

                cur = cur.next

            j += 1
            new_head_ = new_head_.next
        return new_list

    def copyRandomList1(self, head: "Node") -> "Node":
        # 使用哈希表处理
        if not head:
            return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)  # 对象可以作为 dict 的 key!!!!
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]

    def copyRandomList2(self, head: "Node") -> "Node":
        if not head:
            return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res  # 返回新链表头节点


if __name__ == "__main__":
    s = Solution()

    list1 = Node(7)
    list1.random = None
    list1.next = Node(13)
    list1.next.random = list1
    list1.next.next = Node(11)
    list1.next.next.random = Node(1)
    list1.next.next.next = Node(10)
    list1.next.next.next.random = list1.next.next
    list1.next.next.next.next = list1.next.next.random
    list1.next.next.next.next.random = list1
    list1.next.next.next.next.next = None

    # [[3,null],[5,17],[4,null],[-9,6],[-10,3],[5,15],[0,11],[6,null],
    # [-6,16],[3,16],[-6,11],[9,12],[-2,1],[-3,11],[-1,10],[2,11],
    # [-3,null],[-9,7],[-2,4],[-8,null],[5,null]]

    list2 = Node(3)
    list2.next = Node(5)
    list2.next.next = Node(4)

    new_list = s.copyRandomList1(list1)

    print(s.get_list(new_list))
