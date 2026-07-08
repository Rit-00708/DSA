class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is already in the map and within the current window
            if current_char in char_map and char_map[current_char] >= left:
                # Move the left pointer past the previous occurrence
                left = char_map[current_char] + 1
            
            # Update or insert the character's newest index
            char_map[current_char] = right
            
            # Calculate the window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length