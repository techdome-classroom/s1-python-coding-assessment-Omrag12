class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
          if not grid:
               return 0
          def dfs(grid, i, j):
            # Check if we're out of bounds or at water ('W')
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            
            # Mark this cell as visited by setting it to 'W'
            grid[i][j] = 'W'
            
            # Explore the neighboring cells (up, down, left, right)
            dfs(grid, i - 1, j)  # up
            dfs(grid, i + 1, j)  # down
            dfs(grid, i, j - 1)  # left
            dfs(grid, i, j + 1)  # right
        
        # Main logic to count the number of islands
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  # If we find unvisited land ('L')
                    dfs(grid, i, j)    # Perform DFS to mark the entire island
                    islands += 1       # Increment the island count
        
        return islands              
        return 0
