class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = int(len(nums)/2)
        my_dict = {}

        for number in nums:
            if number not in my_dict:
                my_dict[number] = 1
            else:
                my_dict[number]+=1

        for i, x in my_dict.items():
            if x > limit:
                return i

        