class Solution:
    def solve(self, nums):
        nums.sort()

        if len(nums) <= 1:
            return False

        if nums[len(nums)-1] > (nums[len(nums)-2] * 2):
            return True
        
        return False
