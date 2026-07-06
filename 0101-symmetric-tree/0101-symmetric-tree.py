# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # An empty tree is technically symmetric
        if not root:
            return True
            
        # Helper function to compare two subtrees as mirror images
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # Base Case 1: Both sides are empty, meaning they match
            if not t1 and not t2:
                return True
            # Base Case 2: Only one side is empty, meaning a structural mismatch
            if not t1 or not t2:
                return False
            # Base Case 3: The values don't match
            if t1.val != t2.val:
                return False
                
            # Recursive step: 
            # Check left-of-left vs right-of-right AND right-of-left vs left-of-right
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
            
        # Initialize the comparison with the root's left and right children
        return isMirror(root.left, root.right)