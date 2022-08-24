class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = nums[0]
        num2 = float("Inf")
        num3 = float("Inf")
        
        for i in range(1, len(nums)):
            if nums[i] < num1:
                num1 = nums[i]
                
            elif num1 < nums[i] and nums[i] < num2:
                num2 = nums[i]
            
            elif num2 < nums[i] and nums[i] < num3:
                num3 = nums[i]
                
        if num3 == float("Inf") or num2 == float("Inf"):
            return False
            
        return True