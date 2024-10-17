class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row
        setRow = set()

        # Check each row for unique numbers from 1 to 9
        for row in range(len(board)):
            for col in range(len(board[row])):
                element = board[row][col]
                if element != ".":
                    print(setRow)
                    if element not in setRow:
                        setRow.add(element)
                    # If number is already in the set, then sudoku is invalid return False
                    else:
                        return False
           
            # Empty the set when you finish the row
            setRow.clear()

        # Check col
        setCol = set()

        for col in range(9):
            for row in range(9):
                num = board[row][col]
                if num != ".":
                    if num in setCol:
                        return False
                    setCol.add(num)

            setCol.clear()

        # Check sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                setBox = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        num = board[row][col]
                        if num != ".":
                            if num in setBox:
                                return False
                            setBox.add(num)


        return True
        