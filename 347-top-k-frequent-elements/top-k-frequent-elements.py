class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        for i in nums:
            if i in my_dict.keys():
                my_dict[i] +=1
            else:
                my_dict[i] = 1

        items = sorted(my_dict, key=my_dict.get, reverse=True)
        result = items[:k]
        return result











        
    
        