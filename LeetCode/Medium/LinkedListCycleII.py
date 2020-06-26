# LeetCode Medium
# Detect Linked List Cycle Question


class Solution:

    # After learning about the Floyd cycle detection algorithm, I came back to this question to try it again.
    # Now I've achieved O(n) time and O(1) space, an improvement from the dictionary approach below.
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        pointer1 = head
        pointer2 = head

        while True:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer2 is None or pointer1 is None:
                return None
            else:
                pointer2 = pointer2.next
                if pointer2 is None:
                    return None
            if pointer1 == pointer2:
                break

        pointer1 = head
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

    # With the dictionary approach, achieve O(n) time complexity, O(n) space complexity
    # id() can give us the identity of an object, which has to be unique so we can use it for the dictionary key
    def detectCycle2(self, head: ListNode) -> ListNode:
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