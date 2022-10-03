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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            # Update maxSum
            maxSum = max(maxSum, node.val + left + right)
            # Path with greatest sum
            return node.val + max(left, right)
        
        maxSum = float("-inf")
        helper(root)
        return maxSum
            
            