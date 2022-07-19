from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        answer = []

        for col in range(len(grid[0])):

            answer.append(self.find_path(0, col, grid))

        return answer

    def find_path(self, row, col, grid):

        if row >= len(grid):
            return col

        if grid[row][col] == 1:
            if (col + 1 >= len(grid[0])) or (grid[row][col] + grid[row][col + 1] == 0):
                return -1

            return self.find_path(row + 1, col + 1, grid)

        if grid[row][col] == -1:

            if (col - 1 < 0) or (grid[row][col] + grid[row][col - 1] == 0):
                return -1

            return self.find_path(row + 1, col - 1, grid)

