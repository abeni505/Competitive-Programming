# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        
        if not flag:
            return 

        new_slow = head

        while new_slow and fast:
            if new_slow == fast:
                break

            new_slow = new_slow.next
            fast = fast.next

        return new_slow