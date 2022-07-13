class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for i in range(len(s)):

            mapping_value = map1.get(s[i])

            if not mapping_value:

                if not map2.get(t[i]):
                    map1[s[i]] = t[i]
                    map2[t[i]] = s[i]
                    continue

                else:
                    return False

            if mapping_value == t[i]:
                continue
            else:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("abcd", "aaef"))
