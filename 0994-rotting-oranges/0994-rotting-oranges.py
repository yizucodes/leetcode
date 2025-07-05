from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if thre is fresh oranges --> return -1
        # if all oranges are rotten --> 0

        # all empty cells --> 0

        q = deque()
        res = 0
        
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        # unreacheable fresh --> -1

        # find all the cells that have rotten 2
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
    
        # edge case

        # traverse level by level


        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q and fresh > 0:
            for _ in range(len(q)):  # Process one level
                r, c = q.popleft()
                # Check 4 directions
                # If fresh orange found:
                #   - Make it rotten
                #   - Add to queue
                #   - Decrease fresh count

                for dr, dc in directions:
                    newR, newC = dr + r, dc + c
                # check boundaries
                    if (0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1):
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh -= 1
            
            res += 1  # Increment time after each level

        # After while loop:
        if fresh > 0:
            return -1  # Unreachable fresh oranges
        return res

        

