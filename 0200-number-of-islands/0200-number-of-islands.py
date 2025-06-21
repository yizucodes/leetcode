class Solution:
   def numIslands(self, grid: List[List[str]]) -> int:
       # Check if grid is empty or has no columns
       if not grid:
            return 0
       
       # Initialize island count to 0
       numI = 0

       def dfs(row, col):
           rows, cols = len(grid), len(grid[0])

           # Base case: check if row is out of bounds (negative or >= grid height)
           if row < 0 or col >= cols:
                return

           # Base case: check if col is out of bounds (negative or >= grid width) 
           if col < 0 or row >= rows:
                return
           # Base case: check if current cell is water ('0') or already visited
           if grid[row][col] == '0':
                return
           # If any base case is true, return immediately
           
           # Mark current cell as visited by changing '1' to '0'
           grid[row][col] = '0'
           
           # Recursively explore the cell above (row-1, col)
           dfs(row - 1, col)
           
           # Recursively explore the cell below (row+1, col)
           dfs(row + 1, col)

           # Recursively explore the cell to the left (row, col-1)
           dfs(row, col - 1)
           
           # Recursively explore the cell to the right (row, col+1)
           dfs(row, col+1)

       # Loop through every row in the grid
       for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Loop through every column in the current row
                # If current cell contains unvisited land ('1')
                # Increment island counter (found a new island)
                # Call DFS to sink/mark this entire connected island
                if grid[i][j] == '1':
                    numI += 1
                    dfs(i, j)

       
       # Return total number of islands found
       return numI