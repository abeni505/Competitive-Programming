class Solution:
    def pivotInteger(self, n: int) -> int:
        
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 2)

        for i in range(1,n+1):
            prefix[i] = prefix[i - 1] + i

        prefix = prefix[1:]
        
        for j in range(n , 0 , -1):
            suffix[j] = suffix[j + 1] + j

        suffix = suffix[1:n + 1]

        for i in range(n):
            if prefix[i] == suffix[i]:
                return i + 1

        else:
            return -1 
