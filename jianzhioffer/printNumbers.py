from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        result = []

        if n <= 0:
            return result

        for i in range(1, 10 ** n):
            result.append(i)

        return result


if __name__ == '__main__':
    n = input('Please input the x and n: ')
    solution = Solution()
    print(solution.printNumbers(int(n)))