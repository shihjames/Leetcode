"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def getClonedNode(node):
            if node:
                if node in node_dict:
                    return node_dict[node]
                else:
                    cloned = Node(node.val)
                    node_dict[node] = cloned
                    return cloned
        
        if not head:
            return None
        new_head = Node(head.val)
        node_dict = {head: new_head}
        cur = head
        new_cur = new_head
        while cur:
            new_cur.next = getClonedNode(cur.next)
            new_cur.random = getClonedNode(cur.random)
            new_cur = new_cur.next
            cur = cur.next
        
        return new_head
