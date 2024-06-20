class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def checker( min_dist, position, m):
            count = 1
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
      
      
        position.sort()
   
        left, right = 1, position[-1] - position[0]
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if checker(mid, position, m):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best

       