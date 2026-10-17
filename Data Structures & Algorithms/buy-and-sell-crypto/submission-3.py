class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPtr = 0
        sellPtr = 1
        maxProfit = 0
    
        while buyPtr < sellPtr and sellPtr < len(prices):

            if prices[sellPtr] < prices[buyPtr]:
                buyPtr = sellPtr
                sellPtr = buyPtr + 1
            
            else:
                maxProfit = max(prices[sellPtr] - prices[buyPtr], maxProfit)
                sellPtr += 1
        return maxProfit


        