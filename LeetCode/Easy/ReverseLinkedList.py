# LeetCode Easy
# Reverse Linked List Question
# O(n) time complexity, need to traverse the every element of the list, so n = size of list
# O(1) space complexity, only need two additional variables of prev and temp, no matter size of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    # 1 -> 2 -> 3 -> 4 -> None 
    # None <- 1 <- 2 <- 3 <- 4
    # So nodes maintain their position as above, need to reroute pointers
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev