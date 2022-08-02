class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        length = len(arr)

        if k < 0 or k> length:
            return -1
        

        def partition(arr, l, r, val):
            for i in range(l, r):
                if arr[i] == val:
                    arr[r], arr[i] = arr[i], arr[r]
                    break

            i = l
            for j in range(l, r):
                if arr[j] <= val:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[r] = arr[r], arr[i]
            return i

        def med(arr, l, n):
            temp = []
            for i in range(l, l + n):
                temp.append(arr[i])

            temp.sort()
            return temp[n//2]

        def helper(arr, l, r, k):
            n = r - l + 1
            
            from random import randint
            val = arr[randint(l, r)]

            pos = partition(arr, l, r, val)

            if pos - l == k - 1:
                return arr[pos]

            if pos - l > k - 1:
                return helper(arr, l, pos-1, k)

            return helper(arr, pos + 1, r, k - pos + l - 1)

        return helper(arr, 0, length-1, k)