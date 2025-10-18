# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while list1:
            vals.append(list1.val)
            list1 = list1.next
        while list2:
            vals.append(list2.val)
            list2 = list2.next
            
        sorted_vals = sorted(vals)
        dummy = ListNode()
        curr = dummy

        for v in sorted_vals:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next
