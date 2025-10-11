from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for cols_i in range(9):
            for rows_i in range(9):
                if board[cols_i][rows_i] == ".":
                    continue

                if (
                    board[cols_i][rows_i] in cols[cols_i]
                    or board[cols_i][rows_i] in rows[rows_i]
                    or board[cols_i][rows_i] in squares[(cols_i // 3, rows_i // 3)]
                ):
                    return False

                cols[cols_i].add(board[cols_i][rows_i])
                rows[rows_i].add(board[cols_i][rows_i])
                squares[(cols_i // 3, rows_i // 3)].add(board[cols_i][rows_i])

        return True
