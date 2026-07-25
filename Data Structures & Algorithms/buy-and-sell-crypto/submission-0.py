class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxProfit = 0

        for price in range(len(prices)):
            ptr = price + 1

            while ptr < len(prices):
                profit = prices[ptr] - prices[price]
                maxProfit = max(profit, maxProfit)
                ptr += 1
        return maxProfit
            


        