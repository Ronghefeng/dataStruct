from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = []
        sum_val = 0

        for num in nums:
            sum_val += num

            res.append(sum_val)
        return res