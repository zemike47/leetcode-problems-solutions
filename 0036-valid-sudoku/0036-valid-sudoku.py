class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 boxes indexed by (i//3)*3 + j//3

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                # Calculate box index
                box_index = (i // 3) * 3 + (j // 3)

                # Check row, column, and box
                if (num in rows[i] or
                    num in cols[j] or
                    num in boxes[box_index]):
                    return False

                # Add to sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True  