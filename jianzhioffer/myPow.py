
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if x == 0:
            return x
        if n == 0:
            return 1

        result = 1

        if n < 0:
            x, n = 1/x, -n

        while n:
            if n & 1:
                result *= x

            x *= x
            n >>= 1

        return result

    def myPow2(self, x: float, n: int) -> float:
        '''Result: inf'''
        if x == 0:
            return x
        if n == 0:
            return 1

        for i in range(n):
            x *= x

        return x

    def myPow(self, x: float, n: int) -> float:
        return x ** n

if __name__ == '__main__':
    x, n = input('Please input the x and n: ').split()
    solution = Solution()
    print(solution.myPow(float(x), int(n)))

