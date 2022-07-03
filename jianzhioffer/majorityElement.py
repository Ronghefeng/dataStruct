from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        length = len(nums)

        count_map = {}

        for i in nums:

            counts = count_map.get(i, 0)

            counts += 1

            if counts > length / 2:
                return i

            count_map[i] = counts

    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票记述法
        votes, count = 0, 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x
