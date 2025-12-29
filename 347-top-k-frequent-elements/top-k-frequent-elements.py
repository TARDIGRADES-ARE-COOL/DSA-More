class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        for i in nums:
            if i in my_dict.keys():
                my_dict[i] +=1
            else:
                my_dict[i] = 1

        items = list(my_dict.items())
        items = sorted(items, key=lambda pair: pair[1], reverse=True)


        for i in range(k):
            result.append(items[i][0])

        return result

        
    
        