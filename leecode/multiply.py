from collections import deque


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 竖式乘法

        if num1 == "0" or num2 == "0":
            return "0"

        result = []

        tmp_result = deque()

        for i in range(len(num1) - 1, -1, -1):

            tmp_val = 0

            for j in range(len(num2) - 1, -1, -1):

                tmp_val += int(num1[i]) * int(num2[j])
                tmp_result.insert(0, tmp_val % 10)
                tmp_val = tmp_val // 10

            if tmp_val > 0:
                tmp_result.insert(0, tmp_val)
            result.append(tmp_result)
            tmp_result = deque([0] * (len(num1) - i))

        max_length = max(map(len, result))
        result = list(
            map(
                lambda x: deque([0] * (max_length - len(x))) + x
                if len(x) < max_length
                else x,
                result,
            )
        )
        result = list(map(lambda x: sum(x), list(zip(*result))))

        for i in range(len(result) - 1, -1, -1):

            if result[i] >= 10:

                if i == 0:
                    result.insert(0, result[i] // 10)
                    result[i + 1] %= 10
                    break
                else:
                    result[i - 1] += result[i] // 10

                result[i] %= 10

        result = list(map(lambda x: str(x), result))

        return "".join(result)


if __name__ == "__main__":
    s = Solution()
    print(s.multiply("123456789", "987654321"))
