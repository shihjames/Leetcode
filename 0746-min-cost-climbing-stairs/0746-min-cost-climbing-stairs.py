class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:] + [0]
        for i in range(2, len(dp)):
            choice = min(dp[i-1], dp[i-2])
            dp[i] += choice
        return dp[-1]
            