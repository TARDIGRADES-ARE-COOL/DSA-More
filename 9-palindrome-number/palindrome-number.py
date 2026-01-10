class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        digits_list = [int(d) for d in str(x)]

        return digits_list == digits_list[::-1]