class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float("inf")
        profit = 0
        
        for i in prices:
            minVal = min(i,minVal)
            profit = max(profit,i-minVal)

        return profit