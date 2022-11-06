# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal node_cnt, k_smallest
            
            if not node:
                return
            
            dfs(node.left)
            node_cnt += 1
            
            if node_cnt == k:
                k_smallest = node.val
                return
            
            dfs(node.right)
            
        node_cnt = 0
        k_smallest = None
        dfs(root)
        return k_smallest