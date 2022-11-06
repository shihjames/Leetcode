"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def getClonedNode(node):
            if node is not None:
                if node in nodes:
                    return nodes[node]
                else:
                    new_node = Node(node.val)
                    nodes[node] = new_node
                    return new_node
            else:
                return None
        
        if not head:
            return None
        
        nodes = {}
        new_head = Node(head.val)
        nodes[head] = new_head
        
        cur = head
        new_cur = new_head
        
        while cur:
            new_cur.next = getClonedNode(cur.next)
            new_cur.random = getClonedNode(cur.random)
            
            cur = cur.next
            new_cur = new_cur.next
            
        return new_head