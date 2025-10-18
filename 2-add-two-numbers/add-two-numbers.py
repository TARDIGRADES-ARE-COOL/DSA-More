# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = l1
        dummy2 = l2
        temp1 = []
        temp2 = []

        
        while dummy1:
            temp1.insert(0, dummy1.val)
            dummy1 = dummy1.next
        while dummy2:
            temp2.insert(0, dummy2.val) 
            dummy2 = dummy2.next

        dummystring1 = "".join(str(num) for num in temp1)
        dummystring2 = "".join(str(num) for num in temp2)

        finalvalue = str(int(dummystring1) + int(dummystring2))

        print (finalvalue)

        #reversedvalue = str(finalvalue)[::-1]

        head = None
        for digit in finalvalue:
            node = ListNode(int(digit))  # creates a node with value 8 and next=None
            node.next = head # node.next = None (because head is None)
            head = node # move head to point to this new node
        
        return head


        

        


        

 
