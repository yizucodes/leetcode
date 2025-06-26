class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        """
        Start from the ocean edges
        Pacific: top row + left column
        Atlantic: bottom row + right column


        The ONE rule for traversal:

        Can only move to neighbors with height ≥ current height
        (Going "uphill" or flat from the ocean)


        Find cells reached by BOTH

        Whatever cells both DFS traversals visit = your answer
        
        """

        rows, cols = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def dfs(r, c, visitedSet):

            # mark as visited
            visitedSet.add((r, c))

            # up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc

                # base case: boundary check
                if newR < 0 or newR >= rows:
                    continue
                if newC < 0 or newC >= cols:
                    continue

                # base case: visited
                if (newR, newC) in visitedSet:
                    continue

                # if neighbor >= curr
                    # dfs neighbor
                if heights[newR][newC] >= heights[r][c]:
                    dfs(newR, newC, visitedSet)

        # traverse for pac
        # top left to right
        for r in range(rows):
            dfs(r, 0, pac)
     
        # up to down
        for c in range(cols):
            dfs(0, c, pac)

        # traverse for atl
        # right to left
        for r in range(rows):
            dfs(r, cols - 1, atl)

        # down to up from last cell
        for c in range(cols):
            dfs(rows - 1, c, atl)

        # intersection of atl and pac set is answer
        res = []

        for atlR, atlC in atl:
            for pacR, pacC in pac:
                if (atlR, atlC) == (pacR, pacC):
                    res.append([atlR, atlC])

        return res