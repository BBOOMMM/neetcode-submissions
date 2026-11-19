class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [ [1] * n for _ in range(m) ]
        # visited = [ [False] * n for _ in range(m) ]

        def dfs(i, j):
            if dp[i][j]>1:
                return dp[i][j]

            # visited[i][j] = True
            
            for delta_x, delta_y in [ [-1,0], [1,0], [0,1], [0,-1] ]:
                next_i, next_j = i + delta_x, j + delta_y
                # if next_i < 0 or next_i >= m or next_j < 0 or next_j>= n or visited[next_i][next_j] or matrix[i][j] >= matrix[next_i][next_j]:
                if next_i < 0 or next_i >= m or next_j < 0 or next_j>= n or matrix[i][j] >= matrix[next_i][next_j]:
                    continue
                dp[i][j] = max(dp[i][j], 1+ dfs(next_i, next_j) )
        
            # visited[i][j] = False
            
            return dp[i][j]
        
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(dfs(i, j), ans)

        return ans