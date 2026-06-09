class Solution:
    def isValid(self,s: str) -> bool:
        if len(s) == 1:
            return False
        brackets = {
            '{':'}',
            '[':']',
            '(':')',
            ')':'(',
            ']':'[',
            '}':'{'
            }
        open = ["{","[","("]
        close = [")","]","}"]
        
        arr = []
        
        for i in s:
            if i in open:
                arr.append(i)
            if i in close:
                if len(arr) == 0:
                    return False
                temp = arr.pop()
                print(temp)
                if temp != brackets[i]:
                    return False
        if len(arr) == 0:
            return True
        else:
            return False