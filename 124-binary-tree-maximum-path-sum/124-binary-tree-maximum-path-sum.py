# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            
            curSum = node.val + left + right
            maxSum = max(maxSum, curSum)
            
            return node.val + max(left, right)
        
        maxSum = float("-inf")
        helper(root)
        return maxSum
            
            