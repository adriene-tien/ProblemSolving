class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # non-decreasing order 
        # Time complexity: O(n) time, only need to loop through input nums array once 
        # Space complexity: O(n) since we use a hashmap/dictionary, worst case all elements are unique
        duplicateCheck = {}
        k = 0
        indexTracker = 0
        for i in range(len(nums)):
            if nums[i] not in duplicateCheck: 
                duplicateCheck[nums[i]] = 1
                nums[indexTracker] = nums[i]
                indexTracker += 1
                k += 1