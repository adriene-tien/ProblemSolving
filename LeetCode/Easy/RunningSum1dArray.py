# LeetCode Easy
# Running Sum of 1D Array Question
# O(n) time, O(1) space

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1]+nums[i])
        return runningSum
