class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Iterate backwards from the last index to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is less than 9, we just add 1 and we are done.
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and the loop continues to carry the 1
            digits[i] = 0
            
        # If the loop completes, it means all digits were 9 (e.g., [9, 9, 9])
        # We need to add a 1 at the beginning of the array.
        return [1] + digits