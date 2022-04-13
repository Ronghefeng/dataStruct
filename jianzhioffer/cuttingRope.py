import math

class Solution:
    def cuttingRope1(self, n: int) -> int:
        max_product = 1

        for m in range(2, n + 1):
            count, remainder = divmod(n, m)

            multipliers = self.get_multiplier(count, remainder, m)
            products = self.get_product(multipliers)

            if products > max_product:
                max_product = products

        return max_product

    def get_multiplier(self, count, remainder, m):
        multipliers = []

        for i in range(m):
            num = count + (i < remainder)
            multipliers.append(num)

        return multipliers

    def get_product(self, multipliers):
        result = 1

        for produnct_ in multipliers:
            result *= produnct_

        return result

    def cuttingRope(self, n: int) -> int:

        if n <= 3:
            return n - 1

        a, b = n // 3, n % 3

        # math.pow(3, a) 计算幂，3^a
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)

        return int(math.pow(3, a) * 2)

    def cuttingRope2(self, n: int) -> int:
        '''大数据量'''
        if n <= 3: return n - 1
        a, b, p = n // 3, n % 3, 1000000007
        if b == 0: return 3 ** a % p
        if b == 1: return 3 ** (a - 1) * 4 % p
        return 3 ** a * 2 % p


if __name__ == '__main__':
    n = input('Please input the length of rope: ')
    solution = Solution()
    print(solution.cuttingRope(int(n)))