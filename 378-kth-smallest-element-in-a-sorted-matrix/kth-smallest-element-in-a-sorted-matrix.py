class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        nums = []
        for r in range(n):
            for c in range(n):
                nums.append(matrix[r][c])

        heapify(nums)
        
        for _ in range(k - 1):
            heappop(nums)
       
        return nums[0]