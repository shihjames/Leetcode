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
        if not head:
            return None
        new_head = Node(head.val)
        node_dict = {head: new_head}
        cur = head.next
        new_cur = new_head
        while cur:
            new_cur.next = Node(cur.val)
            node_dict[cur] = new_cur.next
            new_cur = new_cur.next
            cur = cur.next
        cur = head
        new_cur = new_head
        
        while cur:
            if cur.random:
                new_cur.random = node_dict[cur.random]
            else:
                new_cur.random = None
            new_cur = new_cur.next
            cur = cur.next
        return new_head
        
            
            