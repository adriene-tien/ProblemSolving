# LeetCode Medium
# Find Minimum Element in Rotated Sorted Array Question

class Solution:

    # Given that there are no duplicates, the brute force seems pretty straight forward
    # O(n) time complexity, O(1) space complexity (no extra space needed)
    def findMinBF(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                return nums[i]

        return nums[0]

    # attempt to optimize further
    def findMin(self, nums: List[int]) -> int:
        pass

