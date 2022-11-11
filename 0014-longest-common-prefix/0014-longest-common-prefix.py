"""
Time = O(ns)
Sapce = O(1)
where s is the min length of all words
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ""
        
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                res += strs[0][i]
            else:
                return res
        
        return res
                