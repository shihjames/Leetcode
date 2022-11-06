# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(m*n)
Space = O(m+n)
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
                
            if sameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
            
        def sameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            
            if (node1 is None or node2 is None) or (node1.val != node2.val):
                return False
            
            return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
        
        return dfs(root)
        