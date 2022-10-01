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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if not node:
                return None
            traverse(node.left)
            traverse(node.right)
            postorder.append(node.val)
            
        postorder = []
        traverse(root)
        
        return postorder