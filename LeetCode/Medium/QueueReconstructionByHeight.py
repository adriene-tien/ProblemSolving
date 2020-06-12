# LeetCode Medium 
# Queue Reconstruction By Height Question 
# I did this question through the June LC Challenge 
# Time complexity: O(nlogn) as we use the sorted() method. the sorted method is "Timsort" which is apparently a variation of merge sort. 
# So the sorted() time complexity is O(nlogn) and overtakes the for loop of n iterations at large values. O(nlogn + n) -> O(nlogn)
# Space complexity: O(n) since we use a return queue list and a sorted queue, both of size n. O(n+n) -> O(n)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        retQueue = []
        for i in range(0, n): 
            retQueue.append([])
        
        sortedQueue = sorted(people, key=lambda x:(-x[0],x[1]))
        for i in range(0, n): 
            index = sortedQueue[i][1] 

            # even the empty array elements get pushed and increase the list size, so pop after insertion
            if (retQueue[index] != []): 
                retQueue.insert(index, sortedQueue[i])
                retQueue.pop()
            else: 
                retQueue[index] = sortedQueue[i]
        
        return retQueue

    # I needed to experiment again with how the sorted() function works here to figure out the approach. 
    # Using the key variation made it easy to start out with
    def test(self): 
        people = [[5,2], [7,0], [5,0], [6,1], [4,4], [7,1]]
        sortedQueue = sorted(people, key=lambda x:(-x[0],x[1])) #first element is sorted in the reverse order, second is in normal order
        
        print(sortedQueue)
        people2 = [[5,2], [5,0], [5,1]]
        sortedQueue = sorted(people2, key=lambda x:x[1])
        print(sortedQueue)

test1 = Solution()
test1.test()