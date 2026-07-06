class Solution:
    def isValid(self, s: str) -> bool:
        # A list to act as our stack
        stack = []
        
        # A dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped opening bracket doesn't match the current closing bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty at the end, all brackets were matched properly
        return not stack
        