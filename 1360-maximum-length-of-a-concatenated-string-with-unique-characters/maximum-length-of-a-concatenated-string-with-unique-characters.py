class Solution:
    def maxLength(self, arr: List[str]) -> int:

        max_len = 0
        n = 2**(len(arr))

        for i in range(n):
            bit = i
            curr = []
    
            for j in range(len(arr)):
                if bit & (1<<j):
                    curr.extend(arr[j])

            if len(set(curr)) == len(curr):
                max_len = max(max_len , len(curr))
            
        return max_len

        