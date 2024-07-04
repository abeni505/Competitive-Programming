# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head
        right=head.next
        run_sum=0
        while right is not None :
            if right.val !=0:
                run_sum+=right.val
                right=right.next
            elif right.val ==0:
                left.next.val=run_sum
                left=left.next
                run_sum=0
                left.next=right.next
                right=right.next
        left.next=None
        return head.next
        



        
        