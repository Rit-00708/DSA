class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases: the square root of 0 is 0, and 1 is 1.
        if x < 2:
            return x
        
        # The square root of any number x >= 2 will always be <= x // 2.
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            
            if squared > x:
                # mid is too large, search the lower half
                right = mid - 1
            elif squared < x:
                # mid is too small, search the upper half
                left = mid + 1
            else:
                # Exact square root found
                return mid
                
        # When the loop ends, 'right' will point to the largest integer 
        # whose square is less than or equal to x.
        return right