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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Create a queue to store nodes in order
        queue = deque([root])
        
        res = []
        
        # Iterate throught the tree in up -> down left -> right order
        while queue:
            # Create an array to store nodes in the same level
            level_nodes = []
            # Pop out all nodes in the queue and push their children (if exists)
            for i in range(len(queue)):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Add the array of nodes in the same level to the res
            res.append(level_nodes)
            
        return res