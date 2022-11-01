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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level):
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
        if not root:
            return []
        res = []
        dfs(root, 0)
        return res
        
        
#         res = []
#         if not root:
#             return res
#         queue = deque([root])
#         # BFS
#         while queue:
#             level = []
#             for i in range(len(queue)):
#                 cur = queue.popleft()
#                 level.append(cur.val)
#                 if cur.left:
#                     queue.append(cur.left)
#                 if cur.right:
#                     queue.append(cur.right)
#             res.append(level)
        
#         return res
                    