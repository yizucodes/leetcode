class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                # For each grid where is land
                if grid[row][col] == 1:
                    squarePeri = 4
                    # Check upper cell
                    if row > 0 and grid[row - 1][col] == 1:
                        squarePeri -= 1
                    # Check lower cell
                    if row < len(grid) - 1 and grid[row + 1][col] == 1:
                        squarePeri -= 1
                    # Check left cell
                    if col > 0 and grid[row][col - 1] == 1:
                        squarePeri -= 1
                    
                    # Check right cell
                    if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                        squarePeri -= 1
        
                    peri += squarePeri
        
        return peri

        
    



        


    


        

