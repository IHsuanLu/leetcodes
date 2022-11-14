from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max((price - min_price), profit)
        
        return profit if profit > 0 else 0