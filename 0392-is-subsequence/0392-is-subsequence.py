"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        queue = deque(list(s))
        
        for i in range(len(t)):
            if t[i] == queue[0]:
                queue.popleft()
                if len(queue) == 0:
                    return True
        
        return False