# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return list1
        
        if list1 == None and list2 != None:
            return list2
        
        if list1 != None and list2 == None:
            return list1

        dummyList = ListNode(0)
        cur = dummyList
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                dummyList.next = list1
                list1 = list1.next
            else:
                dummyList.next = list2
                list2 = list2.next
            dummyList = dummyList.next 
        
        if list1 != None:
            dummyList.next = list1
        
        if list2 != None:
            dummyList.next = list2

        return cur.next