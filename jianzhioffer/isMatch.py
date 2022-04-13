class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s) + 1, len(p) + 1
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1

        for i in range(2, m, 2):
            # 空字符串匹配情况
            if dp[0][i - 2] and p[i - 1] == '*':
                dp[0][i] = 1

        for i in range(1, n):
            for j in range(1, m):

                if p[j - 1] == '*':
                    # dp[i][j - 1]：* 前一个字符出现 1 次的情况
                    # dp[i][j - 2]：* 前一个字符出现 0 次的情况
                    # dp[i - 1][j] and s[i - 1] == p[j - 2]：如 abbb 与 ab* 匹配
                    # dp[i - 2][j] and p[j - 2] == '.'：
                    if dp[i][j - 1] or dp[i][j - 2] or (dp[i - 1][j] and s[i - 1] == p[j - 2]) or (dp[i - 2][j] and p[j - 2] == '.'):
                        dp[i][j] = 1

                else:

                    if (dp[i - 1][j - 1] and s[i - 1] == p[j - 1]) or (dp[i - 1][j - 1] and p[j - 1] == '.'):
                        dp[i][j] = 1

        return bool(dp[n - 1][m - 1])


if __name__ == '__main__':
    s, p = input('Please input the s and p: ').split()
    solution = Solution()
    print(solution.isMatch(s, p))
