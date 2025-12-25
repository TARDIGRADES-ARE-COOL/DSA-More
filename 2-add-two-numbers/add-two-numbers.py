class Solution:
    def addTwoNumbers(self, l1, l2):
        total = ListNode()
        head = total
        pointer1 = l1
        pointer2 = l2
        carry = 0

        # both lists still have nodes
        while pointer1 is not None and pointer2 is not None:
            curr = pointer1.val + pointer2.val + carry
            carry = curr // 10
            digit = curr % 10

            total.val = digit

            pointer1 = pointer1.next
            pointer2 = pointer2.next

            if pointer1 is not None or pointer2 is not None:   # <-- small change: OR
                total.next = ListNode()
                total = total.next

        # l1 leftover
        while pointer1 is not None:
            curr = pointer1.val + carry
            carry = curr // 10
            digit = curr % 10

            total.val = digit
            pointer1 = pointer1.next

            if pointer1 is not None:                          # create next only if needed
                total.next = ListNode()
                total = total.next

        # l2 leftover
        while pointer2 is not None:
            curr = pointer2.val + carry
            carry = curr // 10
            digit = curr % 10

            total.val = digit
            pointer2 = pointer2.next

            if pointer2 is not None:
                total.next = ListNode()
                total = total.next

        # final carry
        if carry:
            total.next = ListNode(carry)

        return head
