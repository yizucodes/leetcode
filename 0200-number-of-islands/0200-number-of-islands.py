class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numI = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # boundaries we are in the grid
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            # return if it's a 0
            if grid[r][c] == "0":
                return

            # update grid with 0
            grid[r][c] = "0"

            # visit top, down, left and right with dfs
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # find first "1", numI += 1, call dfs
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numI += 1
                    dfs(row, col)

        return numI