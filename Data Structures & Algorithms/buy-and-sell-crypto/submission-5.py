class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        for i,val in enumerate(prices):
            for j in prices[i+1:]:
                if j < val:
                    continue
                maxVal = max(maxVal,j-val)
        return maxVal