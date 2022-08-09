class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2:
            return []
        
        v = tomatoSlices//2
        
        x = v - cheeseSlices
        y = 2 * cheeseSlices - v
        
        if x < 0 or y < 0:
            return []
        
        v2 = 2*y + 4*x
        
        if x + y == cheeseSlices and v2 == tomatoSlices:
            return [x, y]
        
        return []