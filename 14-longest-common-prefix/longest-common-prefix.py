class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # if the list is empty
            return ""
        
        # Start by assuming the whole first word is the prefix
        prefix = strs[0]
        
        # Compare this prefix with every other word
        for word in strs[1:]:
            # While the current word does not start with the prefix,
            # remove the last letter from prefix
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # cut off the last letter
                
                # If prefix becomes empty, no common prefix
                if prefix == "":
                    return ""
        
        # When loop finishes, prefix is the common part
        return prefix