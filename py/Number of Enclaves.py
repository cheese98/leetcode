class Solution:
    def recursive(self, grid, p, q):
        grid[p][q] = 0
        size = 1
        if p > 0 and grid[p - 1][q] == 1:
            size += self.recursive(grid, p - 1, q)
        if p < self.m - 1 and grid[p + 1][q] == 1:
            size += self.recursive(grid, p + 1, q)
        if q > 0 and grid[p][q - 1] == 1:
            size += self.recursive(grid, p, q - 1)
        if q < self.n - 1 and grid[p][q + 1] == 1:
            size += self.recursive(grid, p, q + 1)
        return size
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        if self.m <= 2 or self.n <= 2:
            return 0
        sum_val = 0
        for i in range(0, self.m):
            if grid[i][0] == 1:
                self.recursive(grid, i, 0)
            if grid[i][self.n - 1] == 1:
                self.recursive(grid, i, self.n - 1)
        for j in range(0, self.n):
            if grid[0][j] == 1:
                self.recursive(grid, 0, j)
            if grid[self.m - 1][j] == 1:
                self.recursive(grid, self.m - 1, j)

        for i in range(1, self.m - 1):
            for j in range(1, self.n - 1):
                if grid[i][j] == 1:
                    sum_val += self.recursive(grid, i, j)
        return sum_val
