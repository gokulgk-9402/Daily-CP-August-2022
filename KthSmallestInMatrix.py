import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        min_heap = []
        for row in matrix:
            for ele in row:
                heapq.heappush(min_heap, ele)

        for i in range(k-1):
            heapq.heappop(min_heap)

        return min_heap[0]