# LeetCode Medium
# Find The Duplicate Number Question
# Constraints: Read only array, less than O(n^2) time complexity, O(1) space


class Solution:

    # I watched videos on the Floyd cycle detection (tortoise & hare) algorithm before being able to do this
    # O(n) time as the tortoise will never loop through the cycle more than once before meeting the hare
    # O(1) space as no hash map / set was used to look up duplicates
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]

        pointer1 = nums[0]
        pointer2 = nums[0]

        while True:
            pointer1 = nums[pointer1]
            pointer2 = nums[nums[pointer2]]
            if pointer1 == pointer2:
                break

        pointer1 = nums[0]
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]

        return pointer1

    # the below two simple solutions violate some of the constraints so aren't accepted by LeetCode
    # want to include them anyways
    # hash map / set implementation: O(n) time but also O(n) space which violates the constraints
    def findDuplicate2(self, nums: List[int]) -> int:
        checkDup = {}
        n = len(nums)

        for i in range(0, n):
            if nums[i] in checkDup:
                return nums[i]
            else:
                checkDup[nums[i]] = 1

    # this sorts the array, violating the read-only property of it (cannot be modified)
    # this is O(nlogn) time complexity and O(1) space. This is less than O(n^2) but constraint is still violated
    def findDuplicate3(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
