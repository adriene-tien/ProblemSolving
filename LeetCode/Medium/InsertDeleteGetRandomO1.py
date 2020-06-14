# LeetCode Medium 
# Insert Delete Get Random O(1) Question 


# this is a brute force approach. from submission details, there are far faster submissions, gotta fix something 
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {} #implement as a dictionary for checking 
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set: 
            return False 
        else: 
            self.set[val] = 1
            return True 
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set: 
            self.set.pop(val)
            return True 
        else: 
            return False 
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.set.keys()))