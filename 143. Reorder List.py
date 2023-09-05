# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        
        second=slow.next
        prev=slow.next=None
        
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp


        head1,head2=head,prev
        while head2:
            temp1,temp2=head1.next,head2.next
            head1.next=head2
            head2.next=temp1
            head1,head2=temp1,temp2

        
