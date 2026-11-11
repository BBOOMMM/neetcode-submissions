class Solution:
    def subrob(self, start, end, nums):
        if end - start == 0:
            return nums[start]
        dp = [0] * (end - start + 1)
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start+1])
        for i in range(2, end - start + 1):
            dp[i] = max( nums[start+i]+dp[i-2], dp[i-1] )
        return dp[end-start]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1:
            return nums[0]
        ans1 = self.subrob(0, n-2, nums)
        ans2 = self.subrob(1, n-1, nums)
        return max(ans1, ans2)
