class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
      
        hashset = set(fronts+backs) - set(a for a, b in zip(fronts,backs) if a == b)
    
        return min(hashset) if hashset else 0