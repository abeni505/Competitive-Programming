# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(minheap,(node.val ,node))
        
        dummy = curr = ListNode()
        while minheap:
            val , node = heappop(minheap)

            if node.next:
                heappush(minheap, (node.next.val, node.next))
            
            curr.next = node
            curr = curr.next 

        return dummy.next