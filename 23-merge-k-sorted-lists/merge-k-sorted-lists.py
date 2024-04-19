# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(minheap,(node.val , i, node))
        
        dummy = curr = ListNode()
        while minheap:
            val , indx, nod = heappop(minheap)

            if nod.next:
                heappush(minheap, (nod.next.val, indx, nod.next))
            
            curr.next = nod
            curr = curr.next 

        return dummy.next