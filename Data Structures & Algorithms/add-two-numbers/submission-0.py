# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            total = first + second + carry
            digit = total % 10
            carry = math.floor(total/10)
            cur.next = ListNode(digit)

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


