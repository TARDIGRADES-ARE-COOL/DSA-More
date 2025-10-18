from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        y = []
        for num in nums:
            if num not in y:
                y.append(num)
                
        # Update the original list in-place with the unique elements
        nums[:] = y
        
        # Return the count of unique elements
        return len(y)
    

    
    
        