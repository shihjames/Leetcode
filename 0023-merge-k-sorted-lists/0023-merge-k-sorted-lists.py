# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Time = O(nlog(k))
Space = O(n)
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        cur = dummy
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
            
        while heap:
            node_val, index = heappop(heap)
            cur.next = ListNode(node_val)
            cur = cur.next
            lists[index] = lists[index].next
            
            if lists[index]:
                heappush(heap, (lists[index].val, index))
            
        return dummy.next
            