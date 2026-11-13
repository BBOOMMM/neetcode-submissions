class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp = [[0] * n for _ in range(m)]
        dp = [0] * n

        dp[0] = grid[0][0]
        for c in range(1, n):
            dp[c] = grid[0][c] + dp[c-1]

        for r in range(1, m):
            for c in range(0, n):
                if c-1>=0:
                    dp[c] = grid[r][c] + min( dp[c], dp[c-1] )
                else:
                    dp[c] = grid[r][c] + dp[c]
        
        return dp[n-1]
