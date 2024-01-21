class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        Total = sum(nums)
        left_sum = 0
        n = len(nums)
        output = []
        for i in range(n):
            right_sum = Total - nums[i] - left_sum

            left = abs(left_sum - nums[i] * i)
            right= abs(right_sum - nums[i] * (n - 1 - i))

            output.append(left + right)

            left_sum += nums[i] 
        
        return output
        