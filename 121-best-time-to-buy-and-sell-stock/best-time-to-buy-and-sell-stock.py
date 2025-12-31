class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0

        for n in prices:
            if n< min_price:
                min_price = n 
            else:
                best = max(best, n - min_price)
        return best