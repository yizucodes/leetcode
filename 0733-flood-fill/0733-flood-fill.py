class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.
        startingColor = image[sr][sc]
        if startingColor == color:
            return image

        # dfs
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):

            # boundary checks
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return 

            # base case: startingColor same as cell color
            # return
            if startingColor != image[r][c]:
                return

            # modify in place to color
            image[r][c] = color

            directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
            # dfs up, down, left and right
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                dfs(newR, newC)

        dfs(sr, sc)
        return image