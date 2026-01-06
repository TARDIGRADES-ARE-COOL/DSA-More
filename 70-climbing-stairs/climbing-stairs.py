class Solution:
    def climbStairs(self, n: int) -> int:
        stored = [0,1,2]

        if n in stored:
            return stored[n]
        
        if n is None:
            return

    


        for i in range(3, n+1):
            ways = stored[i-1] + stored[i-2]
            stored.append(ways)

        return stored[-1]
        