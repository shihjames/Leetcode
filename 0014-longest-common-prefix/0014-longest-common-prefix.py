class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        
        for s in strs:
            min_len = min(min_len, len(s))
        
        prefix = ""
        for i in range(min_len):
            cur_char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != cur_char:
                    return prefix
            prefix += cur_char
        
        return prefix
                