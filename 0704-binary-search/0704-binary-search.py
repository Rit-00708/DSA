class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Find the middle index (prevents potential overflow in other languages)
            mid = left + (right - left) // 2
            
            # Check if the target is at the middle
            if nums[mid] == target:
                return mid
            # If target is greater, ignore the left half
            elif nums[mid] < target:
                left = mid + 1
            # If target is smaller, ignore the right half
            else:
                right = mid - 1
                
        # Target was not found in the array
        return -1