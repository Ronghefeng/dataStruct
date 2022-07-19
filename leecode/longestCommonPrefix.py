from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""

        for i in range(len(strs[0])):

            for item in strs[1:]:
                if len(item) <= i:
                    return result

                if item[i] != strs[0][i]:
                    return result
            else:

                result += strs[0][i]

        return result
