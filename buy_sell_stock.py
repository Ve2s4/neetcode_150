from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        profit = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            if buy <= sell:
                profit = max(profit, sell - buy)
                r += 1
            else:
                l = r

        return profit

        
sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))