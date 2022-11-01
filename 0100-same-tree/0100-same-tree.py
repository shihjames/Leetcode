# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = O(h)
"""
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p_node, q_node):
            if not p_node and not q_node:
                return True
            if not p_node or not q_node:
                return False
            if p_node.val != q_node.val:
                return False
            else:
                return True
            
        queue = deque([(p, q)])
        while queue:
            p_node, q_node = queue.popleft()
            if not check(p_node, q_node):
                return False
            
            if p_node and q_node:
                queue.append((p_node.left, q_node.left))
                queue.append((p_node.right, q_node.right))
        
        return True
        
#         if not p and not q: 
#             return True
        
#         if not p or not q:
#             return False
        
#         if p.val != q.val:
#             return False
        
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)