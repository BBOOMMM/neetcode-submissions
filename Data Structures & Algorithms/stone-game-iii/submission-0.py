class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i] 表示从第 i 个石头开始, 当前玩家能领先对手的最大分数
        n = len(stoneValue)
        dp = [float('-inf')] * (n+1)
        dp[n] = 0  # 没有石头可以拿
        for i in range(n-1, -1, -1):
            # 拿一个
            dp[i] = stoneValue[i] - dp[i+1]
            # 拿两个
            if i+2 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] - dp[i+2])
            # 拿三个
            if i+3 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3])
        # print(dp)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] == 0:
            return "Tie"
        else:
            return "Bob"