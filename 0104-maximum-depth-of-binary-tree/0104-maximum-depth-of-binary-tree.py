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
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        depth = 0
        
        while stack:
            cur, cur_depth = stack.pop()
            if cur:
                depth = max(depth, cur_depth)
                stack.append((cur.left, cur_depth+1))
                stack.append((cur.right, cur_depth+1))
        
        return depth
        
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    