class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current numeral is smaller than the next one, it's a subtraction case (e.g., IV)
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            # Otherwise, it's standard addition
            else:
                total += roman_map[s[i]]
                
        return total