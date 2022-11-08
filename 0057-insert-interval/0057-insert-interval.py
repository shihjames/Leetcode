"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            
            else:
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]
        
        res.append(newInterval)
        
        return res