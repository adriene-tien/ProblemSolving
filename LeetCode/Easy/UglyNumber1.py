# LeetCode Easy
# Ugly Number I Question: Lead up to Ugly Number II

class Solution:

    # Negative numbers are not ugly numbers
    # just keep dividing the number through until a number which is not divisible by 2, 3, or 5 is reached
    # break from loop and if this number isn't 1 which is the base ugly number, then it is NOT ugly
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num <= 6:
            return True

        while num > 1:
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