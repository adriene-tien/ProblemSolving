# LeetCode Medium
# Search In Rotated Sorted Array Question

class Solution:

    # CURRENTLY EXCEEDS TIME LIMIT, PLAN ON COMING BACK TOMORROW OR STH. this passes the default test case at least
    # binary search approach should be O(log(n)) time
    # if else block is technically O(1) but is realistically very inefficient, this is what needs to be worked around
    # e.g. [4, 5, 6, 7, 0, 1, 2]
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minBound = 0
        maxBound = n - 1
        while minBound < maxBound:
            indexCheck = (minBound + maxBound) // 2
            if nums[indexCheck] == target:
                return indexCheck

            if nums[indexCheck] > target and nums[indexCheck] > nums[0] > target:
                minBound = indexCheck
            elif nums[indexCheck] > target > nums[0] and nums[indexCheck] > nums[0]:
                maxBound = indexCheck
            elif target < nums[indexCheck] < nums[0] and target < nums[0]:
                maxBound = indexCheck
            elif target > nums[indexCheck] > nums[0] and target > nums[0]:
                minBound = indexCheck
            elif nums[indexCheck] < target and nums[indexCheck] < nums[0] < target:
                maxBound = indexCheck
            elif nums[indexCheck] < target < nums[0] and nums[indexCheck] < nums[0]:
                minBound = indexCheck

        return -1

