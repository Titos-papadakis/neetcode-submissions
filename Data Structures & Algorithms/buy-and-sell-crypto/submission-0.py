class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=-1
        max_profit=0
        for sell_price in prices:
            if buy_price==-1:
                buy_price=sell_price
            elif sell_price<buy_price:
                buy_price=sell_price
            elif sell_price>buy_price:
                if max_profit<sell_price-buy_price:
                    max_profit=sell_price-buy_price
        return max_profit
