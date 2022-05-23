class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0 for j in range(n)] for i in range(m)]
        k = k % (m * n)
        x = k // n
        y = k % n
        for i in range(m):
            for j in range(n):
                res[x][y] = grid[i][j]
                y += 1
                if y == n:
                    y = 0
                    x += 1
                if x == m:
                    x = 0
        return res
