class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestforeach = [nums[0]] #-2,-1,-4,0,-1,1,2,-3,1

        for i in range(1,len(nums)):
            largestforeach.append(max(nums[i], nums[i] + largestforeach[i-1]))
            

        return max(largestforeach)



        

        