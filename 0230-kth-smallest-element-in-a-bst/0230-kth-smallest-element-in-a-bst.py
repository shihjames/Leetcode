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
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal count, k_smallest
            if node:
                dfs(node.left)
                count += 1
                if count == k:
                    k_smallest = node.val
                    return 

                if count < k:
                    dfs(node.right)
        
        k_smallest = None
        count = 0
        dfs(root)
        return k_smallest