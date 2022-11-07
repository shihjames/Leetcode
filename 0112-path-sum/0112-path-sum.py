# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, root.val)])
        
        while queue:
            for i in range(len(queue)):
                node, cur_sum = queue.popleft()
                if node.left:
                    queue.append((node.left, cur_sum + node.left.val))
                
                if node.right:
                    queue.append((node.right, cur_sum + node.right.val))
                
                if not node.left and not node.right:
                    if cur_sum == targetSum:
                        return True
        
        return False