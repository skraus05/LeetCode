# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(0)
        finalList = mergedList
        while list1 and list2:
            if list2.val < list1.val:
                finalList.next = list2
                list2 = list2.next
            else:
                finalList.next = list1
                list1 = list1.next
            finalList = finalList.next
        if list1:
            finalList.next = list1
        if list2:
            finalList.next = list2
        return mergedList.next