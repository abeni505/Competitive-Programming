class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def cmp(a , b):
            if a == b: return 0
            if a > b : return 1
            return -1
        
        n = len(arr)
        max_len = 1
        left = 0
        
        for right in range(1, n):
            check = cmp(arr[right-1],arr[right])
            if check == 0: 
                left = right
            elif right == n-1 or check * cmp(arr[right],arr[right+1]) != -1:
                max_len = max(max_len , right - left + 1)
                left = right
                
        return max_len