class Solution:
    def numSteps(self, s: str) -> int:
        
        count = 0
        num = int(s, 2)
      
        while num > 1:
    
            if num % 2:
                num += 1
            else:
                num //= 2
            count += 1

        return count