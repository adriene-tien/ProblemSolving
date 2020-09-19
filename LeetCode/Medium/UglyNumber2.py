# LeetCode Medium 
# Ugly Number II 
# An ugly number is a number whose prime factors only include 2, 3, 5. can be represented like (2^i * 3^j * 5^k)

class Solution:

    # the optimized solution, O(n) time and O(n) space 
    # Store the ugly numbers in an array and keep an index tracker for each 2, 3, and 5 multiplier 
    # Essentially we are multiplying 2, 3, and 5 with a previous ugly number but we cannot move the indexes together 
    def nthUglyNumberProper(self, n: int) -> int:
        # 1 is the first ugly number 
        uglyNumTracker = [1]
        iInd, jInd, kInd = 0, 0, 0
        
        while n > len(uglyNumTracker): 

            iCalc = 2*uglyNumTracker[iInd]
            jCalc = 3*uglyNumTracker[jInd]
            kCalc = 5*uglyNumTracker[kInd]

            uglyNum = min(iCalc, jCalc, kCalc)
            
            if uglyNum == iCalc: 
                iInd += 1 
            elif uglyNum == jCalc: 
                jInd += 1 
            else: 
                # uglyNum == kCalc 
                kInd += 1
            
            if uglyNum == uglyNumTracker[-1]:
                continue 
            else: 
                uglyNumTracker.append(uglyNum)
        
        return uglyNumTracker[-1]
            

    # brute force solution. currently too slow, so implement an optimization.
    # probably has to do making use of a dictionary to check whether it's divisible by a number that's been added to it
    # coming back to this soon
    def nthUglyNumber(self, n: int) -> int:
        if n <= 6:
            return n

        uglyNum = 6
        for i in range(6, n):
            while True:
                uglyNum += 1
                if self.isUgly(uglyNum):
                    break
        return uglyNum

    # isUgly function from UglyNumberI as a helper function
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num <= 6:
            return True

        while num > abs(1):
            check = 0
            if num % 2 == 0:
                check = 1
                num = num / 2
            if num % 3 == 0:
                check = 1
                num = num / 3
            if num % 5 == 0:
                check = 1
                num = num / 5
            if check == 0:
                break

        if num != 1:
            return False
        else:
            return True