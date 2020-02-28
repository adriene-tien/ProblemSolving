# LeetCode Easy
# Merge Two Sorted Lists Question: Linked Lists
# Suppose m and n are the number of nodes (length) of linked list 1 and 2 respectively
# Time complexity is therefore O(m+n) since we need to go through every node of both list
# Space complexity: O(1), we just create a single dummy node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:  # l2.val < l1.val
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # handles the case where one list is longer than the other, so there are leftover nodes to process
        if l1:
            cur.next = l1
            l1 = l1.next
        elif l2:
            cur.next = l2
            l2 = l2.next

        return head.next