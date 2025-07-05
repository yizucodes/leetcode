class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            # 1. Create two sets

            atl = set()
            pac = set()
            ROWS, COLS = len(heights), len(heights[0])

            # 2. Define DFS function  

            def dfs(r, c, visited, prevHeight):
                # boundary check
                if r < 0 or r >= ROWS:
                    return
                if c < 0 or c >= COLS:
                    return

                # if visited return
                if (r ,c) in visited:
                    return

                currH = heights[r][c]
                # currH < preHeight --> return
                if currH < prevHeight:
                    return

                # mark as visited the position
                visited.add((r, c))

                # call dfs positions in grid: up, down, left, right
                directions = [(1,0), (-1,0), (0, -1), (0, 1)]
                for newR, newC in directions:
                    newR = r + newR
                    newC = c + newC
                    dfs(newR, newC, visited, currH)

            # 3. DFS from Pacific boundaries
            # 0,0 top to down and left to right
            for row in range(ROWS):
                dfs(row, 0, pac, heights[row][0])
            
            for col in range(COLS):
                dfs(0, col, pac, heights[0][col])

            # 4. DFS from Atlantic boundaries
            # bot to top, right to left
            for row in range(ROWS):
                dfs(row, COLS - 1, atl, heights[row][COLS-1])
            
            for col in range(COLS):
                dfs(ROWS - 1, col, atl, heights[ROWS-1][col])

            # 5. Return intersection
            res = []
            for r, c in (atl & pac):
                res.append([r,c])
            
            return res