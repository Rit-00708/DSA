class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store numbers and their corresponding indices
        num_map = {}
        
        # enumerate() allows us to loop through both the index (i) and the value (num) simultaneously
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if we have already seen the complement
            if complement in num_map:
                # If found, return the index of the complement and the current index
                return [num_map[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_map[num] = i
            
        # Return an empty list if no solution is found
        return [] 