# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        current_bad = None
        while l<=r:
            m = int((l+r)//2)

            if isBadVersion(m) == False:
                l = m+1
            elif isBadVersion(m) == True:
                current_bad = m
                r = m -1
        return current_bad
        
        