class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        todo = []
        length = len(str(n))
        
        num = 1
        
        while len(str(num)) <= length:
            if len(str(num)) == length:
                todo.append(num)
            num = num * 2
        
        ctr1 = Counter(str(n))
        
        for ele in todo:
            ctr2 = Counter(str(ele))
            if ctr2 == ctr1:
                return True
            
        return False