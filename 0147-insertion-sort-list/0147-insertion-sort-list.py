# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newnode = ListNode()
        curr = head
        while curr:
            prev = newnode
            while prev.next and curr.val >= prev.next.val:
                prev = prev.next

            curr.next, prev.next, curr = prev.next, curr, curr.next

        return newnode.next
