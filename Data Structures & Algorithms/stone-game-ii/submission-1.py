class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i][m] 表示从第 i 个到最后一个石头, 限制为 m 的情况下，先手领先后手的分数
        n = len(piles)
        dp = [[float('-inf')] * (n+1) for _ in range(n+2)]
        for m in range(1, n+1):
            dp[n+1][m] = 0
        for i in range(n, 0, -1):
            for m in range(1, n+1):
                residuals = n - i + 1
                takesum = 0
                for x in range(1, 2*m+1):
                    if x > residuals:
                        break
                    takesum += piles[i-1+x-1]
                    dp[i][m] = max(dp[i][m], takesum - dp[i+x][max(m,x)])
        for row in dp:
            print(row)
        # A - B = x
        # A + B = y
        return (dp[1][1] + sum(piles)) // 2