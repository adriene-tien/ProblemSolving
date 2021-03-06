# HackerRank Medium
# Write A Function question: Leap Year Logic
# O(1) time complexity, O(1) space complexity. Input will only ever be one number, anyways.

def is_leap(year):
    leap = False
    if year % 4 != 0:
        return leap
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return leap
        else:
            return True


year = int(input())
print(is_leap(year))
