from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        total = 0
        for val in nums:
            total += val
        left_sum = 0
        for index, val in enumerate(nums):
            if val + 2 * left_sum == total:
                return index
            left_sum += val
        return -1


if __name__ == "__main__":
    s = Solution()

    for val, result in [
        ([1, -1, 0, 0, 0, 1, -1], 2),
        ([1, 2, 3], -1),
        ([1, 7, 3, 6, 5, 6], 3),
        ([2, 1, -1], 0),
    ]:
        print("输出值：%s   预期值：%s" % (s.pivotIndex(val), result))
