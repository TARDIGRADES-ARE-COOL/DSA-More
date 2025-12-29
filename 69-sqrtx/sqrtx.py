class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        
        for i in range(x):
            if i * i > x:
                return i-1

        return x -1
        