from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        possible = 0
        n = len(arr)

        for i in range(n):
            if i > n - possible - 1:
                break

            if arr[i] == 0:
                if i == n - possible - 1:
                    arr[n - 1] = 0
                    n -= 1
                    break

                possible += 1

        last = n - possible - 1

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible] = 0
                possible -= 1
                arr[i + possible] = 0

            else:
                arr[i + possible] = arr[i]        

a = [1,0,2,3,0,4,5,0]
Solution().duplicateZeros(a)
print(a)
            