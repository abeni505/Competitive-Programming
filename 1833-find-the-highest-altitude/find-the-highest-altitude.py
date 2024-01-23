class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        
        prefix = [0]
        prefix.extend(list(accumulate(gain)))
        
        return max(prefix)