# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(-float("inf"), root, float("inf"))])
        while queue:
            low, node, high = queue.popleft()
            if not low < node.val < high:
                return False
            if node.left:
                queue.append((low, node.left, node.val))
            if node.right:
                queue.append((node.val, node.right, high))
        return True