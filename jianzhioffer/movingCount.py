from queue import Queue


def digitsum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def dfs(i, j, m, n, k, visted) -> int:

            if not (0 <= i < m and 0 <= j < n and (digitsum(i) + digitsum(j) <= k) and visted[i][j] == False):
                return 0

            visted[i][j] = True

            count = dfs(i + 1, j, m, n, k, visted) +\
                    dfs(i, j + 1, m, n, k, visted) +\
                    dfs(i - 1, j, m, n, k, visted) +\
                    dfs(i, j -1, m, n, k, visted) + 1

            return count

        visited = [[False] * n for i in range(m)]

        counts = dfs(0, 0, m, n, k, visited)
        return counts


    def movingCount1(self, m: int, n: int, k: int) -> int:
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)

    def movingCount2(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)


if __name__ == '__main__':
    board = [16, 8, 4]
    solution = Solution()
    print(solution.movingCount(*board))
