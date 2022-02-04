class Solution:
    def DFS(self, x, y, grid):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        if x > 0:
            self.DFS(x-1, y, grid)
        if x < len(grid) - 1:
            self.DFS(x+1, y, grid)
        if y > 0:
            self.DFS(x, y-1, grid)
        if y < len(grid[0]) - 1:
            self.DFS(x, y+1, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.DFS(i, j, grid)
                    count += 1
        return count
