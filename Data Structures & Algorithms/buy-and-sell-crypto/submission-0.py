class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            max_profit=0
            min_no=prices[0]
            i=0
            for i in range (len(prices)):
                min_no=min(prices[i],min_no)
                max_profit=max(prices[i]-min_no,max_profit)
            return max_profit

        