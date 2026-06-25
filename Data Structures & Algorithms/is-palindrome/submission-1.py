class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ","")
        res = "".join(e for e in s if e.isalnum()).lower()
        
        k = 0
        r = len(res) - 1
        
        while r >= k:
            if res[r] != res[k]:
                return False
            r-= 1
            k += 1
        return True