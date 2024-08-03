class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # check if grid is empty
        if not grid:
            return 0

        visited = set()
        numIslands = 0

        def bfs(row, col):
            queue = [(row, col)]
            visited.add((row, col))

            # Explore 4 directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                currRow, currCol = queue.pop(0)

                for dRow, dCol in directions:
                    newRow, newCol = currRow + dRow, currCol + dCol

                    if (0 <= newRow < len(grid) and
                        0 <= newCol < len(grid[0]) and
                        grid[newRow][newCol] == "1" and
                        (newRow, newCol) not in visited):

                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))

        # Iterate over each element
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    numIslands += 1

        return numIslands
