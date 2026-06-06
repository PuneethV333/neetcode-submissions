class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s



    def decode(self,s:str) -> List[str]:
        res = []
        i,j = 0,0

        while i != len(s):
            if(s[j] != "#"):
                j += 1
            else:
                a = s[i:j]
                print(i,j,a)
                count = int(a)
                temp = s[j+1:j+count+1]
                res.append(temp)
                i = j+count+1
                j = i
                
        return res