class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for str in strs:
            temp = "".join(sorted(str))
            x = mp.get(temp,[])
            x.append(str)
            mp[temp] = x
        return list(mp.values())