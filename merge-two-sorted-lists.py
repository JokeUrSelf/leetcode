# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = arr_tmp = ListNode()
            
        while list1 and list2:
            if list1.val <= list2.val:
                arr_tmp.next=list1
                list1 = list1.next
            else:
                arr_tmp.next=list2
                list2 = list2.next
            arr_tmp = arr_tmp.next
        
        arr_tmp.next = list1 if list1 else list2

        return arr.next
