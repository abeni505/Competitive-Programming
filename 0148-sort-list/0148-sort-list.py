# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        Llist=ListNode(0)
        head2=Llist

        for i in arr:
            head2.next=ListNode(i)
            head2=head2.next
        return Llist.next

