class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        
        curr = 0
        i = 0
        ans = []
        
        while curr <= total:
            ans.append(nums[i])
            curr += nums[i]
            total -= nums[i]
            i += 1
            
        return ans 
            