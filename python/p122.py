class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        total_profit = 0
        buy_price = prices[0]
        last_price = prices[0]
        for price in prices:
            if price < last_price:
                # sell yesterday
                total_profit += last_price - buy_price
                # buy today
                buy_price = price

            last_price = price

        # always sell on the final day
        total_profit += last_price - buy_price

        return total_profit

