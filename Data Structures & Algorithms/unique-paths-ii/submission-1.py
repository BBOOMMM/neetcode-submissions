class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] * N

        for c in range(0, N):
            if grid[0][c]:
                break
            else:
                dp[c] = 1

        for r in range(1, M):
            for c in range(0, N):
                if grid[r][c]:
                    dp[c] = 0
                else:
                    if c >= 1:
                        dp[c] += dp[c-1]
            # print(dp)
        return dp[N-1]