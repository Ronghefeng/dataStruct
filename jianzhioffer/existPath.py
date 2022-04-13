from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word:
            return False

        if not (len(board) and len(board[0])):
            return False

        def find_str(i, j, k):

            if not (0 <= i < row and 0 <= j < column) or (board[i][j] != word[k]):
                return False

            if k == (len(word) - 1):
                return True

            board[i][j] = ''

            result = (find_str(i + 1, j, k + 1) or
                      find_str(i, j + 1, k + 1) or
                      find_str(i - 1, j, k + 1) or
                      find_str(i, j - 1, k + 1))

            board[i][j] = word[k]

            return result

        row = len(board)
        column = len(board[0])

        for i in range(row):
            for j in range(column):

                if find_str(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [['a', 'a']]
    word = 'aaa'
    solution = Solution()
    print(solution.exist(board, word))
