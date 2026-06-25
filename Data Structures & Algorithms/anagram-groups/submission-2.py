class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for x in strs:
            sortedS = "".join(sorted(x))
            res[sortedS].append(x)
        return list(res.values())