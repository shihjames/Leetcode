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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(start, end):
            nonlocal preorder_idx
            
            if start > end:
                return None
            
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            
            preorder_idx += 1
            
            root_index = inorder_idx[root_val]
            
            root.left = helper(start, root_index - 1)
            root.right = helper(root_index + 1, end)
            
            return root
        
        inorder_idx = {}
        preorder_idx = 0
        
        for index, node in enumerate(inorder):
            inorder_idx[node] = index
            
        return helper(0, len(inorder) - 1)
        
        