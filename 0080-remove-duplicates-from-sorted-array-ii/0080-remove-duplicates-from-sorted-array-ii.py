class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # i is our "slow pointer" that tracks where to place the next valid number
        i = 0
        
        for n in nums:
            # We automatically accept the first two elements (i < 2)
            # For subsequent elements, we check if it's strictly greater than the element two indices behind
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
                
        return i