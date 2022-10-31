"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            
            # Update minimum price
            if prices[i] < min_price:
                min_price = prices[i]
                
            # Update maximum profit
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit