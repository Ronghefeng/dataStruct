import re
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 超出时间限制
        length = len(nums)

        if length == 0:
            return 0

        min_length = 0

        cur_sum = 0
        i = 0

        while i < length:
            for index, val in enumerate(nums[i:]):

                cur_sum += val

                if cur_sum >= target:

                    if (not min_length) or (min_length and min_length > index + 1):
                        min_length = index + 1

                    if min_length == 1:
                        return 1

                    cur_sum = 0
                    i += 1
                    break
            else:
                i += 1
                break

        return min_length

    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        # 滑动窗口法，O(n)，因为 start 和 end 最多移动 n 次
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
