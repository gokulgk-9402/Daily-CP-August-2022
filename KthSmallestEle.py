class Solution:
    def kthSmallest(self, arr, k):
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
            medians = []

            i = 0
            while i < n//5:
                medians.append(med(arr, l + i * 5, 5))
                i += 1

            while i *5 < n:
                medians.append(med(arr, l+i*5, n%5))
                i += 1

            if i == 1:
                medianofmedians = medians[i-1]
            else:
                medianofmedians = helper(medians, 0, i - 1, i//2)

            pos = partition(arr, l, r, medianofmedians)

            if pos - l == k - 1:
                return arr[pos]

            if pos - l > k - 1:
                return helper(arr, l, pos-1, k)

            return helper(arr, pos + 1, r, k - pos + l - 1)

        return helper(arr, 0, length-1, k)

print(Solution().kthSmallest([12, 3, 5, 7, 4, 19, 26], 3))