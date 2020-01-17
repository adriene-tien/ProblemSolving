# HackerRank Medium
# Merge The Tools! question: String segments and Unique characters
# Where n is the string length:
# O(n) time complexity as we end up checking each character
# O(1) space complexity.
# Worst case is all characters of the alphabet are used, but this caps out at 26 regardless of n -> constant space.


def merge_the_tools(string, k):
    n = len(string)
    tracker = 0
    while tracker != n:
        seg_string = ""
        char_dict = {}
        for i in range(tracker, tracker+k):
            if string[i] in char_dict:
                continue
            else:
                char_dict[string[i]] = 1
                seg_string += string[i]

        print(seg_string)
        tracker += k


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
