from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        # add land to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c))

        # Handle edge case: if no water cells exist, return -1
        if len(q) == 0 or len(q) == ROWS * COLS:
            return -1

        # BFS Phase - spreading distance from all land cells simultaneously
    
        # Set up distance counter starting at 0
        dist = 0
        # Define the 4 directions for neighbor checking

        # up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Main BFS processing loop - continue while queue has cells
        while q:
            
            # Remember current queue size - this represents one distance level
            size = len(q)
            
            # Process exactly that many cells (one complete distance level)
            for _ in range(size):
                # Take one land cell from front of queue
                r, c = q.popleft()
           
                # Check all 4 neighbors of this land cell
                for dr, dc in directions:

                    # Calculate neighbor coordinates
                    new_r, new_c = r + dr, c + dc
                    
                    # If neighbor is valid bounds and is water (0):
                    isValid = 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 0

                    if isValid:
                        # Convert water to land (mark as visited)
                        grid[new_r][new_c] = 1
                        # Add this new land cell to back of queue for next distance level
                        q.append((new_r, new_c))
            
            # After processing entire distance level, increment distance counter
            # Only increment if queue still has cells for next level # WHY AM I DOING THIS?
            if q:
                dist += 1
     
        # Return the final distance (furthest water from any land)
        return dist
       
