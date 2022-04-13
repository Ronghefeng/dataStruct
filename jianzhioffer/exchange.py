from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 快慢指针
        j = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 1:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.exchange(nums))