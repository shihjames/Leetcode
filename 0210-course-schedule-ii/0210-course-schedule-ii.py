class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            
            for neighbor in neighbors[course]:
                if not dfs(neighbor):
                    return False
            
            visited.add(course)
            cycle.remove(course)
            path.append(course)
            return True
            
        neighbors = defaultdict(list)
        for course, prev_course in prerequisites:
            neighbors[course].append(prev_course)
        
        visited = set()
        cycle = set()
        path = []
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []
        
        return path