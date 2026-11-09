class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 1
        
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for n in range(2, n + 1):
            dp[n] = dp[n-1] + dp[n-2]
        return dp[n]