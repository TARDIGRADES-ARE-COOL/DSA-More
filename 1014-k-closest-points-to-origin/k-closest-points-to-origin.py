# import heapq
# from math import *
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         heap = []
#         res = []
        
#         for x , y in points:
#             distance = (x**2) + (y**2)
#             heap.append([distance, [x, y]])

#         heapq.heapify(heap)

#         for i in range(k):
#             distance, cord = heapq.heappop(heap)
#             res.append(cord)

#         return res

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            dist= (x*x) + (y*y)
            minheap.append([dist,x,y])
        heapq.heapify(minheap)
        res=[]
        while k>0:
            dist,x,y= heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res

        