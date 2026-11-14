class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        memo = {}

        def backtrack(index, remaining):


            if remaining == 0:
                return 0

            if remaining < 0:
                return float("inf")
            
            if index >= len(coins):
                return float("inf")

            if (index, remaining) in memo:
                return memo[index, remaining]
            else:
                memo[index, remaining] = min(1 + backtrack(index, remaining - coins[index]), backtrack(index + 1, remaining))

            return memo[index, remaining]
        
        res = backtrack(0,amount)

        if res == float("inf"):
            return -1
        return res


            

            

            
        