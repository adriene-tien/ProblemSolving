# LeetCode Medium
# Reverse Words In A String Question
# Time complexity: reversing is an O(n) operation,
# join is also an O(n) operation and split() on whitespace should also be O(n)
# they are performed sequentially after each other so complexity should come down to O(n+n+n) -> O(n)
# Space complexity: O(n) since we create a temporary list via list comprehension that is
# the length of the input in words


class Solution:

    # can't use reverse(), use [::-1] reverse syntax instead
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in s.split()[::-1]])