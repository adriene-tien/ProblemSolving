# LeetCode Easy
# Maximum Sub-array Question


class Solution:

    # My own successful attempt at solving
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

    # Divide and Conquer Method: Kadane's Algorithm, Dynamic Programming Approach
    # solution is certainly a bit cleaner than above, and is much faster even though both are O(n) time
    # O(n) time, O(1) space
    def maxSubArrayKadane(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        maxsum = nums[0]
        sum = maxsum
        for i in range(1, n):
            # if else block can be simplified to sum = max(sum+nums[i], nums[i])
            if sum + nums[i] > nums[i]:
                sum += nums[i]
            else:
                sum = nums[i]

            if sum > maxsum:
                maxsum = sum

        return maxsum


