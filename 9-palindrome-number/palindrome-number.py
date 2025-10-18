class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        z = []
        y = []
        for c in s:
            z.append(c)
        for i in s :
            y.insert(0,i)
        
        return y==z