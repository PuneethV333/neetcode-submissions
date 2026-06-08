class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVal = 0
        i,j = 0,len(heights)-1
        while j > i:
            maxVal = max(maxVal,(min(heights[i],heights[j])*(j-i)))
            if(heights[i] > heights[j]):
                j-= 1
            else:
                i+=1
        return maxVal