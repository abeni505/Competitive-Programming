class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        x = 0
        for num in nums:
            x ^= num
        
        count = 0
        for i in range(32):
            if (x & (1 << i)) != (k & (1 << i)):
                count += 1
        
        return count