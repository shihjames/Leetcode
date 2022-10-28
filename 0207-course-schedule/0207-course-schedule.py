"""
Time = O(V+E)
Space = O(V+E)
"""
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if neighbors[course] == []:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            
            for prerequisite in neighbors[course]:
                if not dfs(prerequisite):
                    return False

            neighbors[course] = []
            visited.remove(course)
            return True
            
        neighbors = defaultdict(list)
        visited = set()
        
        for post, pre in prerequisites:
            neighbors[pre].append(post)
        
        for courseId in range(numCourses):
            if not dfs(courseId):
                return False
        return True
            
        