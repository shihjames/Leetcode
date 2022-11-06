"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_interval = 0
        counter = {}
        left = 0
        
        for right in range(len(s)):
            if s[right] not in counter:
                counter[s[right]] = 1
            else:
                counter[s[right]] += 1
            
            most_freq = max(counter.values())
            
            while (right - left + 1) - most_freq > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            
            max_interval = max(max_interval, right- left + 1)
            
        return max_interval 