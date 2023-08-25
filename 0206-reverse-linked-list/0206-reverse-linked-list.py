# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack=[]
        curr=head

        while curr:
            stack.append(curr)
            curr=curr.next


        if not stack:
            return None
        newhead=stack.pop()
        curr=newhead
        

        while stack:
            curr.next=stack.pop()
            curr=curr.next
        curr.next=None

        
        return newhead
            
            

        