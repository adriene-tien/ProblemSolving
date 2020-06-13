# LeetCode Medium 
# Sort Colors Question 

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
    
    # Try it in one pass? 
    # this works but time complexity goes up to O(n^2) due to the for loop and nested insert 
    def sortColors2(self, nums: List[int]) -> None: 
        def sortColors(self, nums: List[int]) -> None: 
        n = len(nums)
        indexRed = 0 
        for i in range(0, n): 
            if nums[i] == 0: 
                nums.pop(i)
                nums.insert(0, 0)
                indexRed += 1
            elif nums[i] == 1: 
                nums.pop(i)
                nums.insert(indexRed, 1)
        
