# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if node:
                heappush(heap, -node.val)
                if len(heap) > k:
                    heappop(heap)
                dfs(node.left)
                dfs(node.right)
                
        heap = []
        dfs(root)
        return -heap[0]
        
        