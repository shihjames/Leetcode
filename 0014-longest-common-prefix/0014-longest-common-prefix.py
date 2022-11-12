"""
Time = O()
Sapce = O(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        
        prefix = ""
        
        for i in range(min_len):
            cur_char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != cur_char:
                    return prefix
            prefix += cur_char
        
        return prefix