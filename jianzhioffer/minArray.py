from typing import List


class Solution:
    def minArray1(self, numbers: List[int]) -> int:
        for i in range(len(numbers))[::-1]:
            if numbers[i - 1] > numbers[i]:
                return numbers[i]
        return numbers[0]

    def minArray(self, numbers: List[int]) -> int:
        # 错误!!!! [1, 2, 3]
        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = left + (right - left) // 2

            if numbers[left] < numbers[mid]:
                left = mid + 1

            elif numbers[left] > numbers[mid]:
                right = mid

            else:
                right -= 1

        return numbers[left]

    def minArray2(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]


if __name__ == '__main__':
    array = [3,4,5,1,2]
    solution = Solution()
    print(solution.minArray(array))
