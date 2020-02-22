# LeetCode Medium
# Detect Linked List Cycle Question
# O(n) time complexity, O(n) space complexity


class Solution:

    # id() can give us the identity of an object, which has to be unique so we can use it for the dictionary key
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        indexTracker = 0
        nodeTracker = {}
        while cur:
            if id(cur) not in nodeTracker:
                nodeTracker[id(cur)] = cur  # keep track of index position
            else:
                # found a cycle
                return nodeTracker[id(cur)]
            cur = cur.next
            indexTracker += 1

        return None