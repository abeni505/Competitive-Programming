class Solution:
    def pivotInteger(self, n: int) -> int:
        arr=[i for i in range(1,n+1)]

        for x in range(len(arr)):
            if sum(arr[:x+1])==sum(arr[x:]):
                return x+1

        return -1

        