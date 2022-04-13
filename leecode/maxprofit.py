from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length = len(prices)

        profits = [[0] * length for i in range(length)]

        def get_profit(index, buy_in, nums):

            if not nums:
                return

            for key, value in enumerate(nums):

                profits[index][key + 1] = value - buy_in

        for index, pirce in enumerate(prices):

            get_profit(index, pirce, prices[index:])

        max_profits = []

        return max(max_profits)


if __name__ == '__main__':
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))