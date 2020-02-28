# LeetCode Easy
# Remove Linked List Elements Question
# Time complexity: O(n) where n is the number of nodes in the list
# Space complexity: O(1), no extra space used that grows based on the input size

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if head == None:
            return None

        cur = head
        prev = ListNode(0)
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return head
