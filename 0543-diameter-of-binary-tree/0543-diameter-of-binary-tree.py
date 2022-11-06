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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDiameter(node):
            nonlocal diameter
            if not node:
                return 0
            
            left_diameter = getDiameter(node.left)
            right_diameter = getDiameter(node.right)
            
            diameter = max(diameter, left_diameter + right_diameter)
            
            return max(left_diameter, right_diameter) + 1
        
        diameter = 0
        getDiameter(root)
        return diameter