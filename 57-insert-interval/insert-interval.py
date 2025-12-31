class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i+=1
        while i< len(intervals) and intervals[i][0]<=end:
            start = min(start,intervals[i][0])
            end = max(end, intervals[i][1])
            i+=1
        
        result.append([start,end])

        while i<len(intervals):
            result.append(intervals[i])
            i+=1
        
        return result






            
        