# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
         
        left = None
        right = None

        curr = list1
        i = 1
        while curr:
            if i == a:
                left = curr
            if i == b:
                right = curr.next

            curr = curr.next
            i += 1
        

        left.next = list2
        
        curr = list2
        while curr and curr.next:
            curr = curr.next
        curr.next = right.next

        return list1
        