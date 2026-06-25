class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            target = -nums[i]
            while k > j:
                if target == nums[j]+nums[k]:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+= 1
                    k -= 1
                elif nums[j]+nums[k] < target:
                    j+= 1
                else:
                    k -= 1
        return res