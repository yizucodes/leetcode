class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        atl = set()
        pac = set()

        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, visited, prevHeight):

            # Step 1: Check if we should stop
            if r < 0 or r >= ROWS:
                return

            if c < 0 or c >= COLS:
                return
            # - Already visited this cell?
            if (r, c) in visited:
                return
            # - Height too low? (current height < prevHeight means water can't flow here)
            if heights[r][c] < prevHeight:
                return

            # Step 2: Mark this cell as reachable
            visited.add((r,c))

            # Step 3: Try all 4 directions
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                dfs(newR, newC, visited, heights[r][c])

            # ### **Step 3: DFS from Pacific Edges**
            # - For each Pacific edge cell, do DFS
            # - Mark current cell as "Pacific-reachable"
            # - Explore neighbors where water can flow TO (same or higher elevation)
            # - Continue until you've marked all cells Pacific can reach
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
        
        for r in range(ROWS):
            dfs(r ,0, pac, heights[r][0])

            # Top row: (0, 0), (0, 1), (0, 2), ... (0, COLS-1)

            # Left column: (0, 0), (1, 0), (2, 0), ... (ROWS-1, 0)  

        # ### **Step 4: Find Atlantic Edge Cells**  
        # - Atlantic ocean touches the BOTTOM row and RIGHT column
        # - For every cell in the bottom row: start DFS from there
        # - For every cell in the right column: start DFS from there

        for c in range(COLS):
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # ### **Step 5: Find the Intersection**
        # - Loop through all cells in the heights
        # - If a cell is marked as BOTH Pacific-reachable AND Atlantic-reachable
        # - Add that cell's coordinates to your result list
        res = []
        for (r, c) in (atl & pac):
            res.append([r,c])

        return res