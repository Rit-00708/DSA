class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Continue looping if there are still characters left in a, b, or a carry to add
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add bit from 'a' if available
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Add bit from 'b' if available
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The current bit is total % 2 (0, 1, 2, or 3 -> gives 0 or 1)
            res.append(str(total % 2))
            
            # The new carry is total // 2
            carry = total // 2
            
        # The result is built backwards, so we must reverse it
        return "".join(res[::-1])