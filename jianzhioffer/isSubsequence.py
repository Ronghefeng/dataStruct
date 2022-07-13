from this import s


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        indexs = []
        i = 0

        for s_ in s:

            while i < len(t):

                if t[i] == s_:

                    indexs.append(i)
                    i += 1
                    break

                i += 1

        if len(indexs) < len(s):
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("axc", "ahbgdc"))
