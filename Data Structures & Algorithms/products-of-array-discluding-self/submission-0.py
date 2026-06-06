class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            temp = 1
            for j in range(len(arr)):
                if(i != j):
                    temp *= arr[j]
            
            res.append(temp)
        return res