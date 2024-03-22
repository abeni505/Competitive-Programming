# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = slow = fast = head

        prev = None
        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        if fast:
            slow = slow.next

        while prev:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True

