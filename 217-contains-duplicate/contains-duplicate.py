class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in nums:
            if i in my_dict.keys():
                return True
            else:
                my_dict[i] = i
        return False
        