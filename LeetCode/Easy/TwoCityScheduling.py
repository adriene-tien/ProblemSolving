# LeetCode Easy 
# Two City Scheduling Question 
# June LC Challenge #3

class Solution:

    # my brute force approach involves a two pass approach. see if I can figure out a one pass? 
    # I know that I can calculate the differences between the two costs and choose the lowest N for one city and the highest for the next N
    # Time Complexity: O(nlogn) as it uses sorted() 
    # Space complexity: O(n) as it uses two lists both of size n so O(n+n) -> O(n). There should definitely be a more efficient way to do this
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        splitCount = n/2
        diffTracker = []
        for i in range(0, n): 
            diffTracker.append([costs[i][1]-costs[i][0],i])
        diffSorted = sorted(diffTracker, key = lambda x: x[0])
        total = 0
        for i in range(0, n): 
            indexToLook = diffSorted[i][1]
            if i < splitCount: 
                total += costs[indexToLook][1]
            else: 
                total += costs[indexToLook][0]
        return total 

                