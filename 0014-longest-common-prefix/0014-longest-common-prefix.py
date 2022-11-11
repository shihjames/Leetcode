"""
Time = O(klog(n))
Sapce = O(1)
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
                