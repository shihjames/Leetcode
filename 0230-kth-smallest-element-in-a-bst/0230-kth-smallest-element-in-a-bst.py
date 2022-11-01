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
            if node:
                print(node.val)
                dfs(node.left)
                if len(preorder) == k:
                    return 
                preorder.append(node.val)
                dfs(node.right)
        
        preorder = []
        dfs(root)
        return preorder[-1]