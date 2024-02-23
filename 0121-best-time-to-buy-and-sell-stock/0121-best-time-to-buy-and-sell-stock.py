class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        a, b = 0,0

        while b < len(prices):
            if (prices[b] - prices[a]) > max_profit:
                max_profit = prices[b] - prices[a]
            elif prices[b] - prices[a] < 0:
                a = b
            b += 1
        return max_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        