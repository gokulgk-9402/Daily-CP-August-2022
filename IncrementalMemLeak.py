from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        needed = 1
        
        while needed <= memory1 or needed <= memory2:

            if memory1 >= memory2:
                memory1 -= needed
                
            else:
                memory2 -= needed
                
            needed += 1
            
        return [needed, memory1, memory2]
            
                
            