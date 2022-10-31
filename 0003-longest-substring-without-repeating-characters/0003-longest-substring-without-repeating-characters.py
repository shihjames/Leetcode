class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        l = 0
        cur_ele = set()
        cur_ele.add(s[l])
        for r in range(1, len(s)):
            while s[r] in cur_ele:
                cur_ele.remove(s[l])
                l += 1
            cur_ele.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest