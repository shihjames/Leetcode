# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            nonlocal good_node_cnt
            
            if not node:
                return
            
            if node.val >= cur_max:
                good_node_cnt += 1
            
            cur_max = max(cur_max, node.val)
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
            
        good_node_cnt = 0
        dfs(root, -float("inf"))
        return good_node_cnt
    
#         if not root:
#             return 0
        
#         good_node_cnt = 0
#         queue = deque([(root, -float("inf"))])
        
#         while queue:
#             for i in range(len(queue)):
#                 node, cur_max = queue.popleft()
#                 if node.val >= cur_max:
#                     good_node_cnt += 1
#                     cur_max = node.val
                
#                 if node.left:
#                     queue.append((node.left, cur_max))
                
#                 if node.right:
#                     queue.append((node.right, cur_max))
                    
#         return good_node_cnt
                