class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # no grid
        if not grid:
            return 0

        # recursively check if there is adjacent land
        numI = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            
            # base case: bounds

            if c < 0 or c >= cols:
                return

            if r < 0 or r >= rows:
                return

            # base case: water
            if grid[r][c] == "0":
                return

            # mark as visited by marking as 0
            grid[r][c] = "0"

            # up, down, left, right
            # call dfs again on new coordinates

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # call dfs for each coordinates
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    numI += 1
                    dfs(r, c)
        
        return numI