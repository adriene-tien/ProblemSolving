# LeetCode Easy
# Contains Duplicate Question
# O(n) time complexity, worst case is when all numbers are distinct (infinite numbers)
# O(n) space complexity, worst case is when all numbers are distinct (infinite numbers, new dictionary entry each time)
# Faster than 93% of other submissions, but use of dictionary increases space complexity.
# If I were to use a nested for loop instead, it removes the need for as much space but increases time to O(n^2).


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        int_dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in int_dict:
                int_dict[nums[i]] = 1
            else:
                return True

        return False

