class Solution:
    def __init__(self):
        self.ans = 0
        self.deltax = [0, 0, 1, -1]
        self.deltay = [1, -1, 0, 0]

    def dfs(self, grid, m, n, i, j):
        # 进入的就是符合条件的
        # visited
        grid[i][j] = 2

        for t in range(4):
            nx = i + self.deltax[t]
            ny = j + self.deltay[t]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == 0:
                self.ans += 1
            elif grid[nx][ny] == 1:
                self.dfs(grid, m, n, nx, ny)


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, m, n, i, j)
                    break
        
        return self.ans