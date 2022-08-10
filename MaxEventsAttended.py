import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        es = sorted(events, key = lambda x: x[0])
        l = len(es)
        day = 0
        min_heap = []
        total = max(x[1] for x in events)

        ans = 0
        e_id = 0

        for day in range(1, total + 1):
            while e_id < l and es[e_id][0] == day:
                heapq.heappush(min_heap, es[e_id][1])
                e_id += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                ans += 1

        return ans


print(Solution().maxEvents(events = [[1,2],[2,3],[3,4]]))