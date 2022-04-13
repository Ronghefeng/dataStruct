import numpy

# 构造矩阵
# Method 一
N1 = numpy.zeros([10,10])
# Method 二
N2 = [[0]*10 for i in range(10)]

class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not (matrix and matrix[0]):
            return False

        n = len(matrix)
        m = len(matrix[0])

        j = m - 1
        i = 0
        # 从右上角开始匹配
        while (i < n) and (j >= 0):

            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True

        return False


if __name__ == '__main__':
    matrix = [
        []
    ]
    target = 3
    solution = Solution()
    result = solution.findNumberIn2DArray(matrix, target)
    print(result)
