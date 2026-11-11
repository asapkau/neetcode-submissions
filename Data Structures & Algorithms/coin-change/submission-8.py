class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0


        memo = {}

        def dfs(index, remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float("inf")
            
            if index >= len(coins):
                return float("inf")

            if (index,remaining) in memo:
                return memo[(index,remaining)]
            memo[(index,remaining)] = min(1 + dfs(index, remaining - coins[index]), dfs(index + 1, remaining))

            
            return memo[(index,remaining)]


        res = dfs(0,amount)

        if res == float("inf"):
            return -1
        return res

        


        
        