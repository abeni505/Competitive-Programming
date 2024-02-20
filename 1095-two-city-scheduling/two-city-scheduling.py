class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs , key = lambda x: abs(x[1]-x[0]) , reverse = True)
        n = len(costs)
    
        a = b = total = 0
        for x , y in costs:
            if a == n//2 or b == n//2:
                if a == n//2:
                    total += y
                else:
                    total += x
            else:
                if x < y:
                    total += x
                    a += 1
                else:
                    total += y
                    b += 1
            
        return total