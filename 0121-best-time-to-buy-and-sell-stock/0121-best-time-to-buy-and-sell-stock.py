class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Track the lowest price seen so far
        min_price = float('inf')
        # Track the maximum profit we can make
        max_profit = 0
        
        for price in prices:
            # If we find a new lower price, update min_price
            if price < min_price:
                min_price = price
            # If selling today gives a better profit, update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit