class Solution(object):
    def maxSubArray(self, nums):
        maxn = nums[0]
        curr_max = nums[0]

        for i in nums[1:]:
            curr_max = max(curr_max + i, i)
            maxn = max(curr_max, maxn)
        return maxn 

        """
        :type nums: List[int]
        :rtype: int
        """
        