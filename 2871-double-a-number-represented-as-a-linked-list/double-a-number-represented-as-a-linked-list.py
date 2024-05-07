# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        num = []
        curr = head
        while curr:
            num.append(curr.val)
            curr = curr.next
        
        val = 0
        new_curr = None
        for i in range(len(num) - 1, -1, -1):
            new_curr = ListNode(0, new_curr)
            val += num[i] * 2
            new_curr.val = val % 10
            val //= 10

        if val > 0:
            new_curr = ListNode(val, new_curr)
            
        return new_curr