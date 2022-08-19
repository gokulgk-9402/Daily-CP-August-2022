class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        
        occs = list(counter.values())
        occs.sort(reverse=True)
        
        req = len(arr)//2
        ans = 0
        
        while req > 0:
            req -= occs[ans]
            ans += 1
            
        return ans