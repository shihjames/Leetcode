class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] < res[-1][1]:
                if interval[1] > res[-1][1]:
                    continue
                else:
                    res[-1] = interval
            else:
                res.append(interval)
        
        return len(intervals) - len(res)
        