class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

        val_set = set()

        return self.is_happy_num(n, val_set)

    def sum_value(self, n):

        if n < 10:
            return n * n

        sum_value = 0

        while n >= 10:

            digit_val = n % 10

            sum_value += digit_val * digit_val

            n //= 10

        sum_value += n * n

        return sum_value

    def is_happy_num(self, n, val_set):

        if n == 1:
            return True

        if n in val_set:
            return False

        val_set.add(n)

        n = self.sum_value(n)

        return self.is_happy_num(n, val_set)


if __name__ == "__main__":
    s = Solution()

    print(s.isHappy(2))
