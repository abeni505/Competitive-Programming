class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        if len(deck) == 1:
            return False
        count = Counter(deck)

        vals = list(count.values())

    
        if reduce(gcd,vals) == 1:
            return False
        return True
