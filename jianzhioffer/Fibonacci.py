
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

class Solution1:
    # 计算时间过长
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.fib(n -1) + self.fib(n -2))

class Solution2:
    # 动态规划
    def fib(self, n: int) -> int:
        if n<0:
            return -1
        elif n==0:
            return 0;
        elif n==1:
            return 1;
        else:
            dp = []
            dp.append(0)
            dp.append(1)
            for i in range(2,n+1):
                dp_tmp = (dp[i-1] + dp[i-2])%1000000007
                dp.append(dp_tmp)
            return dp[n]

if __name__ == '__main__':
    n = input('Please input n: ')
    solution = Solution()
    print(solution.fib(int(n)))
    print('----end-----')
