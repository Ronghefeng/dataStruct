from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digits_dict = {}
        for num in digits:
            if num in digits_dict.keys():
                continue
            if num == "2":
                digits_dict[num] = ["a", "b", "c"]
            elif num == "3":
                digits_dict[num] = ["d", "e", "f"]
            elif num == "4":
                digits_dict[num] = ["g", "h", "i"]
            elif num == "5":
                digits_dict[num] = ["j", "k", "l"]
            elif num == "6":
                digits_dict[num] = ["m", "n", "o"]
            elif num == "7":
                digits_dict[num] = ["p", "q", "r", "s"]
            elif num == "8":
                digits_dict[num] = ["t", "u", "v"]
            elif num == "9":
                digits_dict[num] = ["w", "x", "y", "z"]

        length_total = len(digits)

        if length_total == 1:
            return digits_dict[digits[0]]

        result = []

        def get_str(index, tmp_str):

            if index == length_total:
                result.append(tmp_str)
                return

            values = digits_dict[digits[index]]

            for i in range(len(values)):
                new_tmp_str = tmp_str + values[i]
                get_str(index + 1, new_tmp_str)
                new_tmp_str = tmp_str

        get_str(0, "")

        return result

    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


if __name__ == "__main__":
    s = Solution()

    print(s.letterCombinations("239"))
