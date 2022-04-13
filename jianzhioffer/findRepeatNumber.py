
class Solution:
    def findRepeatNumber(self, nums):
        count_list = []
        for i in range(0, 100000 + 1):
            count_list.append(0)

        for i in nums:
            count_list[i] += 1
            if count_list[i] > 1:
                return i

def output(nums):

    if isinstance(nums, list):
        for num in nums:
            print(num, end=' ')

    print(nums)

if __name__ == '__main__':
    nums = [2, 2, 3, 3, 9, 5,7]
    solution = Solution()
    results = solution.findRepeatNumber(nums)
    output(results)
