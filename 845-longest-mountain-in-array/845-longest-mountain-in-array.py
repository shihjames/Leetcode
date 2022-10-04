"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        peak, longest = 1, 0
        while peak < len(arr)-1:
            left, right = peak-1, peak+1
            if arr[peak] > arr[peak-1] and arr[peak] > arr[peak+1]:
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right += 1
                longest = max(longest, right - left + 1)
            peak = right
        
        return longest
                