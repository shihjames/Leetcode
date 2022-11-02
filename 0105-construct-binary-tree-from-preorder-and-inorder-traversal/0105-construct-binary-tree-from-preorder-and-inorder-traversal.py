# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildHelper(left, right):
            if left > right:
                return None
            root_val = queue.popleft()
            root = TreeNode(root_val)
            
            root.left = buildHelper(left, inorder_idx[root_val] - 1)
            root.right = buildHelper(inorder_idx[root_val] + 1, right)
            
            return root

        
        inorder_idx = defaultdict(int)
        queue = deque(preorder)
        
        for index, value in enumerate(inorder):
            inorder_idx[value] = index
        
        return buildHelper(0, len(preorder)-1)