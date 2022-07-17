from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 允许多次买入卖出

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

    def maxProfit2(self, prices: List[int]) -> int:
        # 只允许单次买入卖出

        max_profit = 0

        length = len(prices)

        j = 0

        while j < length:

            i = 0

            while i < length:

                if i > j:

                    value = prices[i] - prices[j]

                    if value > max_profit:
                        max_profit = value

                i += 1
            j += 1

        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:

        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == "__main__":
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
