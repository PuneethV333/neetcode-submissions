class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        res= [1]*(len(arr))
        prefix = 1
        for i in range(len(arr)):
            res[i] = prefix
            prefix*=arr[i]
        postfix = 1
        for i in range(len(arr)-1,-1,-1):
            res[i]*=postfix
            postfix *= arr[i]

        return res
