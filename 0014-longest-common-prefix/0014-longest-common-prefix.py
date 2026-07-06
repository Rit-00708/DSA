class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # If the list is empty, there is no common prefix
        if not strs:
            return ""
        
        # Start by assuming the first string is the common prefix
        prefix = strs[0]
        
        # Iterate through the remaining strings
        for s in strs[1:]:
            # While the current string does NOT start with the prefix
            while not s.startswith(prefix):
                # Shorten the prefix by 1 character from the end
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, there is no common prefix at all
                if not prefix:
                    return ""
                    
        return prefix