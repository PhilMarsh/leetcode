# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_dummy_head = ListNode(val=None)

        carry = 0
        left = l1
        right = l2
        result = result_dummy_head
        while left is not None or right is not None:
            digit_sum = carry
            if left is not None:
                digit_sum += left.val
                left = left.next
            if right is not None:
                digit_sum += right.val
                right = right.next

            result.next = ListNode(val=digit_sum % 10)
            carry = digit_sum // 10
            result = result.next

        if carry:
            result.next = ListNode(val=carry)

        return result_dummy_head.next

