class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        right = 0
        count = 0
        cp = capacity
        while right < len(plants):
            op = capacity - plants[right]
            if op >= 0:
                capacity -= plants[right]
                
            else:
                count += 2*right
                capacity = cp - plants[right]
            count += 1
            right += 1
        return count