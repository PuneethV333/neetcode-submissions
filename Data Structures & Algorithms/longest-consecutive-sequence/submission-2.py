class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        arr = list(set(nums))

        maxVal = 0
        for i in arr:
            if i-1 not in arr:
                val = 1
                while i+val in arr:
                    val += 1
                maxVal = max(val,maxVal)
                
            
        return maxVal