class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # keep a pointer at the tail end of the array that swaps elements
        # O(n) time complexity 
        # O(1) space 
        indexTracker = len(nums)-1
        k = 0
        for i in range(len(nums)):
            if nums[i] == val: 
                while nums[indexTracker] == val and indexTracker > i: 
                    indexTracker -= 1
                nums[i] = nums[indexTracker]
                nums[indexTracker] = val
                if nums[i] != val: 
                    k += 1
            else: 
                k += 1
                
            if indexTracker <= i:  
                break

        return k 