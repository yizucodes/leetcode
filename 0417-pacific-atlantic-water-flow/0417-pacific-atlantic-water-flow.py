class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # ### **Step 1: Set Up Your Data Structures**
        # - Create two sets (or boolean grids) to track which cells each ocean can reach
        # - One for Pacific-reachable cells
        # - One for Atlantic-reachable cells
        pac = set()
        atl = set()

        # ### **Step 2: Find Pacific Edge Cells**
        # - Pacific ocean touches the TOP row and LEFT column
        # - For every cell in the top row: start DFS from there
        # - For every cell in the left column: start DFS from there
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            # Step 1: Check if we should stop
            # - Out of bounds?
            # - Already visited this cell?
            # - Height too low? (current height < prevHeight means water can't flow here)

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if (r, c) in visited:
                return
            if heights[r][c] < prevHeight:
                return
            
            # Step 2: Mark this cell as reachable
            visited.add((r, c))
            
            # Step 3: Try all 4 directions
            dfs(r+1, c, visited, heights[r][c])  # down
            dfs(r-1, c, visited, heights[r][c])  # up  
            dfs(r, c+1, visited, heights[r][c])  # right
            dfs(r, c-1, visited, heights[r][c])  # left

        # ### **Step 3: DFS from Pacific Edges**
        # - For each Pacific edge cell, do DFS
        # - Mark current cell as "Pacific-reachable"
        # - Explore neighbors where water can flow TO (same or higher elevation)
        # - Continue until you've marked all cells Pacific can reach
        
        # Top row: (0, 0), (0, 1), (0, 2), ... (0, COLS-1)
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])

        # Left column: (0, 0), (1, 0), (2, 0), ... (ROWS-1, 0)  
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])

        # ### **Step 4: Find Atlantic Edge Cells**  
        # - Atlantic ocean touches the BOTTOM row and RIGHT column
        # - For every cell in the bottom row: start DFS from there
        # - For every cell in the right column: start DFS from there

        for col in range(COLS):
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
        
        for row in range(ROWS):
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        # ### **Step 5: Find the Intersection**
        # - Loop through all cells in the grid
        # - If a cell is marked as BOTH Pacific-reachable AND Atlantic-reachable
        # - Add that cell's coordinates to your result list
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res



