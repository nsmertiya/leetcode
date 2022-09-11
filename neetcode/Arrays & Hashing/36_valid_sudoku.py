class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # create default dict for maintaining a set of numbers for row, column and each square
        rows,col,squares = collections.defaultdict(set),collections.defaultdict(set),collections.defaultdict(set)
        
        # check if each cell value is already present for that row, column or square.
        # if yes, return false else update the set for those respective rows , columns and square
        for row_index in range(9):
            for col_index in range(9):
                value = board[row_index][col_index]
                if value!='.':
                    if (value in rows[row_index]) or (value in col[col_index]) or (value in squares[(row_index//3,col_index//3)]):
                        return False
                    else:
                        rows[row_index].add(value)
                        col[col_index].add(value)
                        squares[(row_index//3,col_index//3)].add(value)
        return True
                        
