class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        mem = {}

        def binary_search(arr, target):
            left = 0
            right = n2 - 1
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    if mid != n2 -1 and arr[mid + 1] == target:
                        left = mid + 1
                    else:
                        return mid + 1
                        
                elif arr[mid] < target:
                    left = mid + 1
                    
                else:
                    right = mid - 1
                    
            return left
                    
        arr2.sort()
        # print(arr2)
        
        ans = []
        
        for ele in arr1:
            if ele in mem:
                ans.append(mem[ele])
            else:
                mem[ele] = binary_search(arr2, ele)
                ans.append(mem[ele])
            
        return ans

print(Solution().countEleLessThanOrEqual([1, 2, 3, 4, 7, 9], 6, [0, 1, 2, 1, 1, 4], 6))