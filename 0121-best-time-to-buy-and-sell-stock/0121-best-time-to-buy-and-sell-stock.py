class Solution(object):
    def maxProfit(self, prices):
        lo = prices[0]
        max_prof = 0
        for i in prices:
            lo = min(lo, i)
            max_prof = max(max_prof, i - lo)
        return max_prof


        """
        :type prices: List[int]
        :rtype: int
        """
        