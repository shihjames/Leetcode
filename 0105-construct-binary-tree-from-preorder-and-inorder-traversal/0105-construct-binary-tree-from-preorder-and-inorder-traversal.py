# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(start, end):
            if start > end:
                return None
            
            root_val = preorder.popleft()
            root = TreeNode(root_val)
            
            root_index = inorder_idx[root_val]
            
            root.left = helper(start, root_index - 1)
            root.right = helper(root_index + 1, end)
            
            return root
            
        
        inorder_idx = {}
        preorder = deque(preorder)
        
        for index, node in enumerate(inorder):
            inorder_idx[node] = index
            
        return helper(0, len(inorder) - 1)
        
        