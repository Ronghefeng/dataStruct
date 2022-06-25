import sys, os

# 导入上级同级目录文件
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from typing import List
from sort import quicksort


class Solution:
    def threeSum(self, nums: List[int]):

        quicksort.Quicksort(nums)

    def ordering(self, nums: List[int]):

        high = len(nums) - 1

        if high <= 0:
            return nums

        low = 0

        while low < high:

            if nums[low] > nums[high]:

                nums[high], nums[low] = nums[low], nums[high]

                high = high - 1

            else:

                low = low + 1

            self.ordering(nums[low : high + 1])

        return nums


if __name__ == "__main__":

    nums = [-1, 0, 1, 2, -1, -4]

    nums = Solution().threeSum(nums)
