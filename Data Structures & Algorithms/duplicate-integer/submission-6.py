class Solution:
    def hasDuplicate(self,arr: list[int]) -> bool:
        return len(set(arr)) != len(arr)

        