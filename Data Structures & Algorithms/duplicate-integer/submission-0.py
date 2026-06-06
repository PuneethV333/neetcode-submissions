class Solution:
    def hasDuplicate(self,arr: list[int]) -> bool:
        withOutDup = set(arr)
        if(len(arr) == len(withOutDup)):
            return False
        return True

        