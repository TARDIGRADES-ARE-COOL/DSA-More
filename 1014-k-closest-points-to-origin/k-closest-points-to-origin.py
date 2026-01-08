import heapq
from math import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for x , y in points:
            distance = (x**2) + (y**2)
            heapq.heappush(heap, [distance, [x, y]])

        for i in range(k):
            distance, cord = heapq.heappop(heap)
            res.append(cord)

        return res





        