# HackerRank Medium
# Piling Up! Question: Arrays/Lists, Comparisons
# Time Complexity O(n) where n = total number of cubes (all tests)
# Space Complexity O(max(m)) where max(m) refers to the most number of cubes for a test out of all tests

from sys import stdin

num_tests = int(input())
for i in range(num_tests):
    failed = False
    num_cubes = int(input())
    cube_line = input()
    cube_stats = [int(elem) for elem in cube_line.split(" ")]
    if cube_stats[0] >= cube_stats[num_cubes - 1]:
        last_val = cube_stats.pop(0)
        num_cubes -= 1
    else:
        last_val = cube_stats.pop(num_cubes - 1)
        num_cubes -= 1

    while num_cubes > 0:
        if (cube_stats[0] >= cube_stats[num_cubes - 1]) and (cube_stats[0] <= last_val):
            last_val = cube_stats.pop(0)
            num_cubes -= 1
        elif (cube_stats[0] < cube_stats[num_cubes - 1]) and (cube_stats[num_cubes - 1] <= last_val):
            last_val = cube_stats.pop(num_cubes - 1)
            num_cubes -= 1
        else:
            print("No")
            failed = True
            break

    if not failed:
        print("Yes")
