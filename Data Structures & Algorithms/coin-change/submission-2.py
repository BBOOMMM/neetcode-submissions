class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 背包问题
        # dp[i][j] 用前 i 个硬币, j个amount
        m, n = len(coins), amount
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if coins[i-1] <= j:
                    # 有用和不用两种
                    # 1 + dp[i][j-coins[i-1]]
                    # dp[i-1][j]
                    # if dp[i][j-coins[i-1]] != -1:
                    #     dp[i][j] = 1 + dp[i][j-coins[i-1]]
                    # elif dp[i-1][j] != -1:
                    #     dp[i][j] = min(dp[i][j], dp[i-1][j])
                    dp[i][j] = min(1 + dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[m][n] != float('inf'):
            return int(dp[m][n])
        else:
            return -1