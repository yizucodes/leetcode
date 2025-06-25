from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        # add to queue for target so rotten ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:    # No fresh oranges (including no oranges at all)
            return 0
        if len(q) == 0:   # Fresh oranges exist but no rotten ones
            return -1

        # left, right, up, down,
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        # bfs
        while q:
            size = len(q)
            rotted = False
        
            # process each element in the queue
            for _ in range(size):
                
                r, c = q.popleft()
              
                # find neighbor coordinates
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc

                    # check for boundary and if meet 1  
                    isValid = 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1

                    if isValid:
                        rotted = True
                        # mark rotten
                        grid[newR][newC] = 2
                        # add rotten to queue for next level processing
                        q.append((newR, newC))
                        # fresh -= 1
                        fresh -= 1
                
            # after each level time += 1
            if rotted:
                time += 1

    
        if fresh == 0:
            return time
        # isolated fresh orange or all oranges are rotten
        else:
            return -1




