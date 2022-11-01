# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, stack):
            nonlocal count
            if node:
                cur_max = 0 if not stack else stack[-1][1]
                if not stack or node.val >= cur_max:
                    count += 1
                    cur_max = node.val
                else:
                    cur_max = stack[-1][1]
                dfs(node.left, stack + [(node.val, cur_max)])
                dfs(node.right, stack + [(node.val, cur_max)])
        
        count = 0
        dfs(root, [])
        return count
            
                