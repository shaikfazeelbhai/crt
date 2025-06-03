class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        temp = [0] * n
        d = d % n
        for i in range(len(arr)):
            temp[(n+d+i) % n] = arr[i]
        for i in range(len(arr)):
            arr[i] = temp[i]
        return arr

arr = [1, 2, 3, 4, 5]
d = 2
print(Solution().rotateArr(arr, d))