# LeetCode Medium
# Kth Largest Element in Array Question
# Searching for some kth max or kth min automatically suggests to me that this is a heap question
# Time complexity: our key operations here are the heapify operation and the pop of the maximum element.
# Pop: O(log(n)), Heapify is O(n). O(n + log(n)) -> O(n) overall time complexity
# Space complexity: O(1)

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        for i in range(0, k):
            kthLargest = heapq._heappop_max(nums)

        return kthLargest
