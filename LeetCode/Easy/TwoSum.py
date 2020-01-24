# LeetCode Easy
# Two Sum Question
# O(n) time complexity
# O(n) space complexity
# Can do nested for loop for O(1) space since that wouldn't make use of dictionary, but increases TC to O(n^2)

class Solution:

    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        num_dict = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in num_dict:
                return [num_dict[difference], i]
            else:
                num_dict[nums[i]] = i