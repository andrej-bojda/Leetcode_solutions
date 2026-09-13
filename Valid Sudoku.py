from typing import List
import collections

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            valid_row = dict()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in valid_row:
                    valid_row[board[i][j]] = 1
                else:
                    return False

        for i in range(len(board)):
            valid_column = dict()
            for e in range(len(board)):
                if board[e][i] == ".":
                    continue
                if board[e][i] not in valid_column:
                    valid_column[board[e][i]] = 1
                else:
                    return False

        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                box_id = (r // 3, c // 3)
                seen_in_this_box = boxes[box_id]
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen_in_this_box:
                    return False
                else:
                    seen_in_this_box.add(val)

        return True