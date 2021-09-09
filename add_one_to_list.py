class Solution:
    def solve(self, nums):
        nums = int("".join(str(num) for num in nums))
        return [int(i) for i in str(nums + 1)]
