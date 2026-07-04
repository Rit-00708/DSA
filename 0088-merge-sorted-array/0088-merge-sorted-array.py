class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set up three pointers
        p1 = m - 1       # Last valid element in nums1
        p2 = n - 1       # Last element in nums2
        p = m + n - 1    # Last position of the entire nums1 array
        
        # Merge elements as long as there are elements left in nums2
        while p2 >= 0:
            # If nums1 still has elements and its current element is larger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Either nums1 is empty, or nums2 has the larger element
                nums1[p] = nums2[p2]
                p2 -= 1
            
            # Move the placement pointer backward
            p -= 1