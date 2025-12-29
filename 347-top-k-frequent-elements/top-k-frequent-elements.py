class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        for i in nums:
            if i in my_dict.keys():
                my_dict[i] +=1
            else:
                        my_dict[i] = 1
        for number, occurrence in my_dict.items():
            if not result:
                result.append(number)
                continue

            pos = 0
            while pos < len(result) and occurrence <= my_dict[result[pos]]:
                pos += 1
            result.insert(pos, number)

        return result[:k]


        
    
        