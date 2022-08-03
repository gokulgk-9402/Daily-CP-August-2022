ef bs(arr, ele):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right)//2
            if arr[mid] == ele:
                return mid

            elif arr[mid] < ele:
                left = mid + 1

            else:
                right = mid - 1
        
        return -1