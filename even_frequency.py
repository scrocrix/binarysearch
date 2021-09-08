class Solution:
    def solve(self, nums):
        lookup = {}

        for num in nums:
            if num not in lookup:
                lookup[num] = 1
                continue
            
            lookup[num] = lookup[num] + 1
        
        for k, i in enumerate(lookup):
            if lookup[i] % 2 != 0:
                return False
        
        return True

