class Solution:
    def twoSum(self,arr: list[int], target: int) -> list[int]:
        i,j = 0,1
    
        while i != len(arr)-1:
            while j != len(arr):
                if arr[i]+arr[j] == target:
                    return [i,j]
                j += 1
            i += 1
            j = i+1
        return []