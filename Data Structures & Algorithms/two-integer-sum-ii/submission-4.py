class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k,r = 0,len(numbers) -1
        
        while r >= k:
            if (numbers[r] + numbers[k]) == target:
                return [k+1,r+1]
            if (numbers[r] + numbers[k]) > target:
                r -= 1
            elif (numbers[r] + numbers[k]) < target:
                k += 1