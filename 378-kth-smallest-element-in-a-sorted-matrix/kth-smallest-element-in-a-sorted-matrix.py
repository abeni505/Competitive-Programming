class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        down = list(merge(*matrix))

        return down[k-1]