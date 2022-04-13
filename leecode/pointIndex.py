
class Solution:
    def pivotIndex(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return -1

        i = 0
        nums_sum = 0
        left_sum = 0

        for n in range(length):
            nums_sum += nums[n]

        for i in range(length):
            if i == 0:
                nums_sum -= nums[0]
            else:
                left_sum += nums[i - 1]
                nums_sum -= nums[i]

            if left_sum == nums_sum:
                return i
            i += 1

        return -1
'''
class Solution:
	def pivotIndex ( self, nums: List[int] ) -> int:
		if len(nums) == 0:
			return -1
		left = 0
		sum = 0
		for num in nums:
			sum += num
		right = sum
		for i in range(len(nums)):
			if i == 0:
				right -= nums[0]
			else:
				right -= nums[i]
				left += nums[i-1]
			if right == left:
				return i
		return -1
'''

if __name__ == '__main__':
    nums = [0,1,0]
    solution = Solution()
    print(solution.pivotIndex(nums))
