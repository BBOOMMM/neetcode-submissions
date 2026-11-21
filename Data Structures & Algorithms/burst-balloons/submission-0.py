class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ [0] * (n+1) for _ in range(n+1) ]
        for i in range(1, n+1):
            dp[i][i] = nums[i-1] * (nums[i-2] if i-2 >=0 else 1) * (nums[i] if i < n else 1)
        for k in range(1, n+1):
            for i in range(1, n+1):
                j = i + k
                if j > n:
                    break
                # 最后一个扎破的气球
                for f in range(i, j+1):
                    mid = nums[f-1] * (nums[i-2] if i-2 >= 0 else 1 ) * ( nums[j] if j < n else 1 )
                    left = dp[i][f-1] if f-1 >= i else 0
                    right = dp[f+1][j] if f+1 <= j else 0
                    dp[i][j] = max( dp[i][j], left + mid + right )
        return dp[1][n]