class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        a , b = nlargest(2,nums)

        return (a - 1) * (b - 1)