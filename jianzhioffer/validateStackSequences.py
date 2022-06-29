class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:

        if len(pushed) == 0 and len(popped) == 0:
            return True

        if len(pushed) != len(popped):
            return False

        i = 0

        while i >= 0 and i < len(pushed) and len(popped) > 0:

            if pushed[i] == popped[0]:

                if i == 0:

                    pushed = pushed[1:]

                else:

                    pushed = pushed[:i] + pushed[i + 1 :]

                    i -= 1

                popped = popped[1:]

            else:

                i += 1

        if len(pushed) == 0 and len(popped) == 0:
            return True

        # print("pushed: %s, poped: %s" % (pushed, popped))

        return False

    def validateStackSequences1(self, pushed: list, popped: list) -> bool:

        stack, i = [], 0
        for num in pushed:

            stack.append(num)  # num 入栈

            while stack and stack[-1] == popped[i]:  # 循环判断与出栈

                stack.pop()

                i += 1

        return not stack


if __name__ == "__main__":

    s = Solution()

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]

    print(s.validateStackSequences(pushed, popped))
