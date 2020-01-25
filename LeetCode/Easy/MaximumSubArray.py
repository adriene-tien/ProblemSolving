# LeetCode Easy
# Maximum Sub-array Question

class Solution:

    # O(n) time complexity solution, avoiding double for loop.
    # O(1) space complexity, only need two variables -> constant.
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        maxsum = nums[0]
        sum = maxsum
        for i in range(1, n):
            if nums[i] > sum and sum < 0:
                sum = nums[i]
                if sum > maxsum:
                    maxsum = sum
            else:
                sum += nums[i]
                if sum > maxsum:
                    maxsum = sum

        return maxsum

    # try divide and conquer method
