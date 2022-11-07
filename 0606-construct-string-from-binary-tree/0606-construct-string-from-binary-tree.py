# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            nonlocal res
            
            if not node:
                return

            res += str(node.val)
            
            if not node.left and not node.right:
                return
            
            res += "("
            dfs(node.left)
            res += ")"
              
            if node.right:
                res += "("
                dfs(node.right)
                res += ")"
        
        res = ""
        dfs(root)
        return res