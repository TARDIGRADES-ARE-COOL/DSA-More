# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        pointer1 = list1
        pointer2 = list2
        result = ListNode()
        head = result

        while pointer1 is not None and pointer2 is not None:
            if pointer1.val<= pointer2.val:
                result.next = ListNode(pointer1.val)
                result = result.next
                pointer1 = pointer1.next
            else:
                result.next = ListNode(pointer2.val)
                pointer2 = pointer2.next
                result = result.next
        while pointer2 is not None:
            result.next = ListNode(pointer2.val)
            pointer2 = pointer2.next
            result = result.next
        while pointer1 is not None :
            result.next= ListNode(pointer1.val)
            pointer1 = pointer1.next
            result = result.next

        return head.next
