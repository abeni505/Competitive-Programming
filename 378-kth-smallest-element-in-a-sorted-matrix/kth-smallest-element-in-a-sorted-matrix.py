class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        down = list(merge(*matrix))

        return nsmallest(k , down)[-1]