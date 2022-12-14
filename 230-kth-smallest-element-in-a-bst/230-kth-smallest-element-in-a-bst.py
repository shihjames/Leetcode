# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = O(h), where h is the height of the tree
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            if not node:
                return None
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
        
        inorder = []
        traverse(root)
        return inorder[k-1]