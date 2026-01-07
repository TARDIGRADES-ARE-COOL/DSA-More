class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(max(nums[i], nums[i]+ result[i-1]))
        
        return max(result)


        