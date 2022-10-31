class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        cur_ele = set()
        # Create a valid interval until it reaches the end
        left, right = 0, 1
        cur_ele.add(s[left])
        while right < len(s):
            while s[right] in cur_ele:
                cur_ele.remove(s[left])
                left += 1
            longest = max(longest, right - left + 1)
            cur_ele.add(s[right])
            right += 1
        return longest