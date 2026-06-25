class Solution:
    def twoSum(self,arr: list[int], target: int) -> list[int]:
        prev = {}

        for i,n in enumerate(arr):
            diff = target-n
            if diff in prev:
                return [prev[diff],i]
            prev[n] = i

        return []