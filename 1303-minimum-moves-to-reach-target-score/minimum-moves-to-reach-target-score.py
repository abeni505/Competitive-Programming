class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        cur = 1
        count = 0
        
        while maxDoubles and target > 1:
            r = target % 2
            target //= 2
            maxDoubles -= 1
            count += 1
            count += r if r else 0
        
    

        return count + target - 1

