class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkValid(block):
            nums = [False] * 9
            for x in block:
                if x == ".":
                    continue
                if nums[int(x) - 1]:
                    return False
                nums[int(x) - 1] = True
            return True
        for i in range(0, 9):
            if not checkValid(board[i]):
                return False
            if not checkValid([board[j][i] for j in range(0, 9)]):
                return False
            if not checkValid([board[(i // 3) * 3 + j][(i % 3) * 3 + k] for j in range(0, 3) for k in range(0, 3)]):
                return False
        return True
