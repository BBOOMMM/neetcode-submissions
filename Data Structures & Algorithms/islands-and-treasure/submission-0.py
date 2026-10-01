class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 多源 BFS
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[False] * n for _ in range(m)]
        WATER, TREASURE, LAND = -1, 0, 2147483647
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # 加入宝箱节点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == TREASURE:
                    q.append((i,j))
        
        dist = 1
        while q:
            len_q = len(q)
            for _ in range(len_q):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny] == LAND:
                        visited[nx][ny] = True
                        grid[nx][ny] = dist
                        q.append((nx, ny))
            dist += 1