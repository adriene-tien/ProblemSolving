# LeetCode Medium
# Kth Largest Element in Array Question
# Searching for some kth max or kth min automatically suggests to me that this is a heap question

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        for i in range(0, k):
            kthLargest = heapq._heappop_max(nums)

        return kthLargest
