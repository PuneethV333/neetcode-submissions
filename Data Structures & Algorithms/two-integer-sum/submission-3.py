class Solution:
    def twoSum(self,arr: list[int], target: int) -> list[int]:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j] == target:
                    return [i,j]

        return []