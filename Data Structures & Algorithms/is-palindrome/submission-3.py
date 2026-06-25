class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [i.lower() for i in s if i.isalnum()]
        res = "".join(res)

        return res == res[::-1]