from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pre_num = None
        count = 0

        for value in nums:
            if value != pre_num:

                nums[count] = value
                pre_num = value
                count += 1

        return count


if __name__ == '__main__':
    solution = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums))