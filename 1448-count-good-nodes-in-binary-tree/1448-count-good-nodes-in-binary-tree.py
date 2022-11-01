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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            nonlocal count
            if node.val >= cur_max:
                count += 1
            new_max = max(cur_max, node.val)
            if node.left:
                dfs(node.left, new_max)
            if node.right:
                dfs(node.right, new_max)
        
        count = 0
        dfs(root, float("-inf"))
        return count
            
                