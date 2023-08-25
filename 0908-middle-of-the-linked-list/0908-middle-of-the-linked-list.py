# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        count=0
        curr=head
        while curr:
            curr=curr.next
            length+=1
        midnode=head
        while count < (length//2) :
            midnode=midnode.next
            count+=1
        return midnode


        