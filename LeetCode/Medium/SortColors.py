# LeetCode Medium 
# Sort Colors Question 
# My brute force solution as well as the one pass solution are included here 

class Solution:

    # My approach: I can just count the number of red, white, blue, then just update the values of the array directly based on the count
    # Cons: has to be two pass. try one pass later
    # Time Complexity: O(n) as it is O(n+n) but for large inputs simplifies to O(n)
    # Space Complexity: O(1) as we are using a constant amount of space each time, no extra array used 
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        numRed = 0 
        numWhite = 0 
        numBlue = 0 
        for i in range(0, n): 
            if nums[i] == 0: 
                numRed += 1
            elif nums[i] == 1: 
                numWhite += 1
            else: 
                numBlue += 1
 
        for i in range(0, n): 
            if i < numRed: 
                nums[i] = 0 
            elif i < numRed+numWhite: 
                nums[i] = 1 
            else: 
                nums[i] = 2


    # I needed to look up the Dutch National Flag Problem to understand the one pass solution 
    # Makes use of three pointers 
    # O(n) time complexity and O(1) space. Always consider multiple pointers for optimizing sorting questions 
    def sortColorsOnePass(self, nums: List[int]) -> None: 
        n = len(nums)
        if n == 0 or n == 1: 
            return 
        low = 0 
        mid = low 
        high = n-1 
        while high >= mid: 
            val = nums[mid]
            if nums[mid] == 0: 
                nums[mid] = nums[low]
                nums[low] = val 
                low += 1
                mid += 1
            elif nums[mid] == 1: 
                mid += 1
            else: 
                nums[mid] = nums[high]
                nums[high] = val 
                high -= 1 
    
    # further notes: Why we increment mid when swapping with low but not high 
    # When swapping a 2 with nums[high], you can get a 1, 0, or 2 in return. incrementing mid 
    # means we never compare this value again, and if we get a 2 in return that means it's left in the middle of the array 
    # Mid and low start out the same as each other and we never get a 2 in return for swapping mid and low, we are left 
    # with 0s and 1s which we actively want to swap. we either swap 0s for 0s which leave no change, or 0s at nums[mid] for 1s 
    # at nums[low] which is the correct way to proceed. 
