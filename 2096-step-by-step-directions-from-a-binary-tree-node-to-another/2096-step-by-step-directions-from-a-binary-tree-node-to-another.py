# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = O(n)
"""
from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s_path = None
        e_path = None
        queue = deque([(root, "")])
        while queue:
            for i in range(len(queue)):
                node, path = queue.popleft()
                if node.val == startValue:
                    s_path = deque(list(path))
                elif node.val == destValue:
                    e_path = deque(list(path))
                if node.left:
                    queue.append((node.left, path+"L"))
                if node.right:
                    queue.append((node.right, path+"R"))
        
        
        while s_path and e_path and s_path[0] == e_path[0]:
            s_path.popleft()
            e_path.popleft()
            
        return "U" * len(s_path) + "".join(e_path)
                
        