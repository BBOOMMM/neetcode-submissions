class Solution:  
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[target] = 1

        for i in range(target, -1, -1):
            if dp[i]:
                for num in nums:
                    if i >= num:
                        dp[i - num] += dp[i]

        return dp[0] 
    # def __init__(self) -> None:
    #     self.cur_sum = 0
    #     self.ans = 0

    # def backtracking(self, nums, target):
    #     if self.cur_sum == target:
    #         self.ans += 1
    #         return 
    #     elif self.cur_sum > target:
    #         return 
        
    #     for i in range(len(nums)):
    #         self.cur_sum += nums[i]
    #         self.backtracking(nums, target)
    #         self.cur_sum -= nums[i]

    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     self.backtracking(nums, target)
    #     return self.ans
