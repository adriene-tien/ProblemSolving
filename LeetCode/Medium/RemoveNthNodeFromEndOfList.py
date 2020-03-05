# LeetCode Medium
# Remove Nth Node from End of List Question: Linked Lists
# My solution does it in one pass - after reaching the end of the list with full Trav I can immediately move to cutting
# the nth node from the list
# Therefore Time Complexity is O(m) where m is the number of nodes in the linked list
# Space complexity: O(1), does not grow with input. Always use the same pointers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 1 and not head.next:
            return None

        sizeCount = 1
        fullTrav = first = second = head
        for _ in range(0, n):
            fullTrav = fullTrav.next
            if fullTrav:
                sizeCount += 1

        if fullTrav:
            while fullTrav.next:
                fullTrav = fullTrav.next
                first = first.next
                second = second.next
                sizeCount += 1

        if n == sizeCount:
            head = head.next
            return head

        for _ in range(0, 2):
            first = first.next

        second.next = first

        return head