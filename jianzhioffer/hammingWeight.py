class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight1(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count


if __name__ == '__main__':
    n = 0o00000000000000000000000000001011
    solution = Solution()
    print(solution.hammingWeight(n))