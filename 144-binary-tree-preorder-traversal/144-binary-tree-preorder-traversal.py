# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if not node:
                return None
            preorder.append(node.val)
            traverse(node.left)
            traverse(node.right)
            
        preorder = []
        traverse(root)
        
        return preorder