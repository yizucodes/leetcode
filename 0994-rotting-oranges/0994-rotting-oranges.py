from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 2: Scan the entire grid
        # - Find all initially rotten oranges and add their positions to queue
        # - Count all fresh oranges
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == 2:
                    queue.append((r,c))
                elif cell == 1:
                    fresh_count += 1

        # Step 2.5: Handle edge case
        # - If no fresh oranges exist, return 0 (already all rotten)
        if fresh_count == 0:
            return 0

        mins = 0
        # Step 3: Main BFS loop - process level by level
        # - While queue has oranges:
        #   - Remember current queue size (this is one time level)
        #   - Process exactly that many oranges:
        #     - Pop orange from queue
        #     - Check its 4 neighbors (up, down, left, right)
        #     - If neighbor is fresh, make it rotten, add to queue, decrease fresh count
        #   - After processing entire level, increment minutes (if queue still has items)
        while queue:
            size = len(queue)
            
            # Track if any oranges rot in this iteration
            level_rotted = False
            
            # process based on size of oranges - level by level
            for _ in range(size):
                r, c = queue.popleft() # pop from an empty deque
             
                # check all 4 neighbors
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                
                    # Check if neighbor is valid and fresh # THIS SHOULD BE INDENTED?
                    if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1):
                        # Your code here: make it rotten, add to queue, decrease fresh_count
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        fresh_count -= 1
                        level_rotted = True
                
            if level_rotted:
                mins += 1
        
        # Step 4: Final check and return
        # - If fresh_count is 0, return minutes
        # - Otherwise return -1 (isolated oranges existed)
        if fresh_count == 0:
            return mins
        else:
            return -1