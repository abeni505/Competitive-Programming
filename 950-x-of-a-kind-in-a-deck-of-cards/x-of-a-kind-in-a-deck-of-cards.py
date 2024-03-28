class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        
        count = Counter(deck)

        vals = list(count.values())

    
        if reduce(gcd,vals) == 1:
            return False
        return True
