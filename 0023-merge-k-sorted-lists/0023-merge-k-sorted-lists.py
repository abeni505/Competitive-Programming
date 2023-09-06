# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedList=[]

            for i in range(0,len(lists),2):
                list1=lists[i]
                if (i+1)<len(lists):
                    list2=lists[i+1]
                else:
                    list2=None
                mergedList.append(self.mergeTwoLists(list1,list2))
            lists=mergedList
        return lists[0]
        
    def mergeTwoLists(self,list1,list2):
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
        