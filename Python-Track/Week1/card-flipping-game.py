class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
      
        hashset = set(fronts+backs)
        
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                hashset.discard(fronts[i])

        if hashset:
            return(min(hashset))
            
        return 0