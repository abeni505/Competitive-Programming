class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()
        

        max_ = 0

        for house in houses:
            min_ = inf
            right = bisect.bisect_left(heaters, house)
            left = right - 1
  
            if right == 0:
                min_ = min(min_,abs( heaters[0] - house))
    
            elif right == len(heaters):
                min_ = min(min_, abs(house - heaters[-1]))
            else:
                min_ = min(min_, min(abs(house - heaters[right]),abs( heaters[left] - house)))

            max_ = max(max_ , min_)
     
        return max_