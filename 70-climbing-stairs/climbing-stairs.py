class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0,1,2] #if n = 1 take 1 step , if n = 2 take 2 step
        if n in steps:
            return steps[n]

        if n is None:
            return None
        
        for index in range(3, n+1):
            next_amount_steps = steps[index-1] + steps[index-2]
            steps.append(next_amount_steps)
        return steps[n]