class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string
        str_x = str(x)
        
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]