class Solution(object):
    def search(self, nums, target):
        
        def binary(left, right):
            if left > right:
                return -1
            mid = (right + left)
            if nums[mid] == target:
                return mid
            # move the left limit up to middle
            elif nums[mid] < target:
                return binary(mid+1, right)
            else:
                return binary(left, mid - 1)
        return binary(0, len(nums)-1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        