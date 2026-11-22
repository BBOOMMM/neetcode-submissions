class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 初始化：s 为空字符串
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    # 普通字符或者 '.'
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]

                else:
                    # '*' 匹配 0 次
                    dp[i][j] = dp[i][j - 2]

                    # '*' 匹配至少 1 次
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
