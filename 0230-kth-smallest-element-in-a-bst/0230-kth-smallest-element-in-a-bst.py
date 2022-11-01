# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                if len(preorder) == k:
                    return 
                preorder.append(node.val)
                dfs(node.right)
        
        preorder = []
        dfs(root)
        print(preorder)
        return preorder[-1]