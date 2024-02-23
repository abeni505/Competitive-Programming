class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        new = sorted(weights[i] + weights[i - 1] for i in range(1,len(weights)))
        
        min_ = sum(new[:k-1])
        max_ = sum(new[len(new) - k + 1: ])
        return max_ - min_