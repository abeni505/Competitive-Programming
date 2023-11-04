class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        output = [0]*(len(gain)+1)
        prefix=0
        for i in range(1,len(gain)+1):
            output[i] = gain[i-1] + prefix
            prefix += gain[i-1]
        
        return max(output)