# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        if not root:
            return right
        queue = deque([root])
        # BFS
        while queue:
            level_right = None
            for i in range(len(queue)):
                cur = queue.popleft()
                level_right = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            right.append(level_right)
        
        return right