from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        while matrix:

            result += matrix.pop(0)

            matrix = list(reversed(list(zip(*matrix))))

        return result
