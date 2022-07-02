from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ["+", "-", "*"]:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1 :])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == "+":
                            res.append(l + r)
                        elif char == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.diffWaysToCompute("2*3-4*5"))
