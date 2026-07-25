class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        buy = 0
        sell = buy + 1
        profit = 0
        maxProfit = 0

        while buy < sell and buy >= 0 and sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
                sell += 1
            
            elif prices[sell] <= prices[buy]:
                buy = sell
                sell = buy + 1
        return maxProfit

