class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            
            # Add 1 if it's the candidate, subtract 1 if it's not
            count += (1 if num == candidate else -1)
            
        return candidate