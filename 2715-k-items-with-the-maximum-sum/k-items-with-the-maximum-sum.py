class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = []
        for i in range(numOnes):
            nums.append(1)
        for j in range(numZeros):
            nums.append(0)
        for x in range(numNegOnes):
            nums.append(-1)
        
        return sum(nums[:k])