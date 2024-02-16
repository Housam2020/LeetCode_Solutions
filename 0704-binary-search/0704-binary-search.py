class Solution(object):
    def search(self, nums, target):
        left, right, mid = 0, len(nums)-1, len(nums)//2
        def find(left, right, target):
            if (left > right):
                return -1

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                find(left, right, target)
            else:
                right = mid -1
                find(left, right, target)

       

        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        else:
            return -1
            

        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        