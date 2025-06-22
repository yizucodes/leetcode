class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxA = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):

            # base case: out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return
            # base case: water or visited
            if grid[r][c] == 0:
                return

            # mark land as 0 to count as visited
            grid[r][c] = 0
            
            # up
            aUp = dfs(r - 1, c)

            # down
            aDown = dfs(r + 1, c)

            # left
            aLeft = dfs(r, c - 1)

            # right
            aRight = dfs(r, c + 1)

            return 1 + aUp + aDown + aLeft + aRight


        # find islands
        for row in range(rows):
            for col in range(cols):
                # do dfs to explore all connected 1s
                if grid[row][col] == 1:
                    islandA = dfs(row, col)
                    maxA = max(maxA, islandA)
                    

        return maxA