class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numI = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):

            # base case
            # boundary checks
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            # if water return
            if grid[r][c] == "0":
                return

            # mark to 1 to 0
            grid[r][c] = "0"

            # call dfs on up, down, right and left
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # find first land
        # increment numI
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    numI += 1
                    dfs(row, col)

        
        return numI

