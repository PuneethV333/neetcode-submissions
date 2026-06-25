class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxVal = 0

        for n in nums:
            if (n-1) not in numSet:
                val = 0
                while (n+val) in numSet:
                    val+=1
                maxVal = max(val,maxVal)

        return maxVal