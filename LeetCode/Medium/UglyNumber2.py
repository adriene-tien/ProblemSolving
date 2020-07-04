class Solution:

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

        check = 0
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