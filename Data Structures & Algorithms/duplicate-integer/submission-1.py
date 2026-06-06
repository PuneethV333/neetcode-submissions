class Solution:
    def hasDuplicate(self,arr: list[int]) -> bool:
       return len(arr) != len(set(arr))

        