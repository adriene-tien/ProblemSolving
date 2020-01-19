# LeetCode Medium
# Longest Substring Without Repeated Characters Question

class Solution:

    # My brute force solution (show an interviewer that I can at least do the base problem).
    # Space complexity is constant O(1) as the dictionary will cap out at 26 characters
    # LeetCode Performance Analysis
    # Memory usage: better than 99.49% of other Python3 submissions
    # Time complexity: only faster than 14.03% of other submissions - makes sense, need to get rid of nested for
    # Time optimized solution seems to involve space trade off?
    def lengthOfLongestSubstringBrute(self, s: str) -> int:
        max_length = 0
        char_dict = {}
        local_length = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in char_dict:
                    char_dict[s[j]] = 1
                    local_length += 1
                else:
                    if local_length > max_length:
                        max_length = local_length
                    local_length = 0
                    char_dict = {}
                    break

        return max_length if max_length > local_length else local_length

    # Sliding window approach (?) can reduce time complexity from O(n^2) to O(n).
    # Managed to drop time complexity from O(n^2) -> O(n) without increasing required memory
    # Introduced last_index variable which helps keep track of repeat windows within a larger repeat window
    # Now faster than 60% of other submissions while still maintaining 99.49% better memory usage than other submissions
    def lengthOfLongestSubstringBetter(self, s: str) -> int:
        max_length = 0
        char_dict = {}
        local_length = 0
        last_index = 0
        for i in range(0, len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = i
                local_length += 1
            else:
                if local_length > max_length:
                    max_length = local_length

                if last_index > char_dict[s[i]]:
                    local_length = i - last_index
                else:
                    local_length = i - char_dict[s[i]]

                if last_index < char_dict[s[i]]:
                    last_index = char_dict[s[i]]

                char_dict[s[i]] = i

        return max_length if max_length > local_length else local_length
