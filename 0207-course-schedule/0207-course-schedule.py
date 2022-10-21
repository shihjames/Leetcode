"""
Time = O(V+E)
Space = O(V+E)
"""
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hasCycle(course):
            if course in checked:
                return False
                
            if course in visited:
                return True
            
            visited.add(course)
            
            cycle = False
            for prerequisite in graph[course]:
                cycle = hasCycle(prerequisite)
                if cycle:
                    break

            checked.add(course)
            visited.remove(course)
            return cycle
            
        graph = defaultdict(list)
        visited = set()
        checked = set()
        
        for post, pre in prerequisites:
            graph[pre].append(post)
        
        for courseId in range(numCourses):
            if hasCycle(courseId):
                return False
        return True
            
        