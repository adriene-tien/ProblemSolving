# LeetCode Medium
# Add Two Numbers Question: Linked Lists
# Time complexity: O(max(m, n)) where m is the number of nodes in list 1, and n is the number of nodes in list 2
# We traverse both at the same time so end up having a cycle that lasts as long as the max size + 1 in the case of carry
# Space complexity: O(max(m, n)) since we create a list of the same size from the addition. Each iteration sees us
# creating a node for cur.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2

        head = cur = ListNode(0)
        carry = 0
        # the very last set of nodes could have a carry e.g. 500+500 = 1000
        while l1 or l2 or carry:
            cur.next = ListNode(0)
            cur = cur.next
            if l1:
                cur.val += l1.val
            if l2:
                cur.val += l2.val
            if carry:
                cur.val += carry

            if cur.val >= 10:
                carry = 1
                cur.val %= 10
            else:
                carry = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next