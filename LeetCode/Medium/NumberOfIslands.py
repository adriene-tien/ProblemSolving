# LeetCode Medium 
# Number of Islands Question 
# Graphing / Matrix 

class Solution:

    # O(n * m) time complexity as we traverse every single element of the matrix where n = length and m = width of matrix 
    # O(1) space if we do not count the matrix, as I do not use any extra array to keep track of discovery. I just set the element itself to a 0
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid is None or len(grid) == 0: 
            return 0 
        
        numIslands = 0 
        # must traverse the entire matrix to be sure of how many islands there are 
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    numIslands += self.dfs(grid, i, j)
                    
        
        return numIslands; 
        
    
    def dfs(self, grid, i, j): 
        if (grid is None) or (i < 0) or (i > len(grid)-1) or (j < 0) or (j > len(grid[i])-1) or (grid[i][j]) == "0": 
            return 0
        
        grid[i][j] = "0"
        
        # check left, right, up, down 
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        # successfully discovered all 1s in area 
        return 1 