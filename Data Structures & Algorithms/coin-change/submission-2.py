class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0

        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float("inf")
            
            if remaining in memo:
                return memo[remaining]
            memo[remaining] = float("inf")
            for coin in coins:
                memo[remaining] = min(1 + dfs(remaining - coin), memo[remaining])

            return memo[remaining]

        res = dfs(amount)

        if res == float("inf"):
            return -1
        return res

        


        
        