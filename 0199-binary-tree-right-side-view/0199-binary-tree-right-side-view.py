# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = O(d)
where d is the diameter of the tree
"""
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Create a queue to store nodes in level order
        queue = deque([root])
        
        right_side_view = []
        
        # Traverse the tree in level order
        while queue:
            # Store nodes in the same level
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                # Push the rightmost node to the result (right_side_view)
                if i == queue_len - 1:
                    right_side_view.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
        return right_side_view
                
            