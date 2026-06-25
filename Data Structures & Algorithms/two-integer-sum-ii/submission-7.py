class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k,r = 0,len(numbers) -1
        
        while r >= k:
            val = numbers[r] + numbers[k]
            if val == target:
                return [k+1,r+1]
                break;
            if val > target:
                r -= 1
            elif val < target:
                k += 1
        return []