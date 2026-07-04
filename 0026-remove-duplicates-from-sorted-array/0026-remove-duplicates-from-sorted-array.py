class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # An empty array has 0 unique elements
        if not nums:
            return 0
            
        # 'write_index' keeps track of where the NEXT unique element should go.
        # It starts at 1 because the very first element (index 0) is always unique to itself.
        write_index = 1
        
        # 'read_index' scans through the array starting from the second element
        for read_index in range(1, len(nums)):
            # If the current element is different from the one right before it, 
            # it means we've found a new, unique number!
            if nums[read_index] != nums[read_index - 1]:
                # Overwrite the duplicate/old value at the write_index with this new unique value
                nums[write_index] = nums[read_index]
                
                # Move the write pointer forward to prepare for the next unique element
                write_index += 1
                
        # The write_index naturally represents the total count of unique elements (k)
        return write_index