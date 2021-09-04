class Solution:
    def solve(self, nums, k):
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            
            if sum < k:
                left = left + 1
            
            if sum > k:
                right = right - 1
            
            if sum == k:
                return True
    
        return False
