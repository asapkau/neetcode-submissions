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
            
            best = float("inf")
            for coin in coins:
                best = min(1 + dfs(remaining - coin), best)
            memo[remaining] = best
            return memo[remaining]

        res = dfs(amount)

        if res == float("inf"):
            return -1
        return res

        


        
        