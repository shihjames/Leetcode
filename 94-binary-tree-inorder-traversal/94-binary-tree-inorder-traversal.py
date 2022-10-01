# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = worst: O(n), average: O(log(n))
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if not node:
                return None
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
            
        inorder = []
        traverse(root)
        
        return inorder