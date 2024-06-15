class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = (1 << 31) - 1
        while b & mask:
            carry = (a & b) << 1
            a ^= b
            b = carry
        return a & mask if b > 0 else a