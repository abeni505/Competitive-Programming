# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # curr=head
        # curr=head
        # while curr:
        #     if curr.head1<=curr.head2:
        #         temp=curr.next
        #         curr1.next
        #         curr.next=curr.head2
        dummy=ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
            
        return dummy.next



        