class Solution:
    def xorOperation(self, n: int, start: int) -> int:
    
        startpoint=start
        res=start

        for i in range(1,n):
            res=res^(startpoint+2*i)
        return res