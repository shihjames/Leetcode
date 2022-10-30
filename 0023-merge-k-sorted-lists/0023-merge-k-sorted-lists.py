# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time = O(nlog(k))
Space = O(1)
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = cur = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 if list1 else list2
            return dummy.next   
        
        length = len(lists)
        if length == 0:
            return None
        interval = 1
        while interval < length:
            for i in range(0, length-interval, interval*2):
                lists[i] = mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]
        
#         dummy = cur = ListNode()
#         heap = []
#         for i in range(len(lists)):
#             if lists[i]:
#                 heapq.heappush(heap, (lists[i].val, i))
        
#         while heap:
#             val, index = heapq.heappop(heap)
#             cur.next = ListNode(val)
#             cur = cur.next
#             lists[index] = lists[index].next
#             if lists[index]:
#                 heapq.heappush(heap, (lists[index].val, index))
        
#         return dummy.next