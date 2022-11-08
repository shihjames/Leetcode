"""
Time = O(nlog(n))
Space = O(1)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        count = 0
        
        for interval in intervals[1:]:
            if interval[0] < prev_end:
                prev_end = min(prev_end, interval[1])
                count += 1
            else:
                prev_end = interval[1]
        
        return count
        