class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1:
            return "0"
        
        val = ceil((2**n - 1)/2)
        
        if k == val:
            return "1"
        
        if k < val: 
            return self.findKthBit(n - 1 , k)
        else:
            check = self.findKthBit(n - 1, 2*val - k) # val  - (k - val)

            return str(int(check) ^ 1)
            

