class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        new = [(abs(i - x) , i) for i in arr]
        heapify(new)

        output = []
        for _ in range(k):
            output.append(heappop(new)[1])
        
        output.sort()
        return output