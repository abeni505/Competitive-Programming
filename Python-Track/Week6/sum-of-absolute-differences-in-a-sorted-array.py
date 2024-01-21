class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        

        prefix = [0]
        suffix = [0]

        for i in range(len(nums) - 1):
            prefix.append(nums[i] + prefix[-1])
        
        for j in range(len(nums) - 1, 0,-1):
            suffix.append(nums[j] + suffix[-1])

        suffix = suffix[::-1]
        output = []
        for k in range(len(prefix)):
            left_sum = abs(prefix[k] - nums[k] * k)
            right_sum = abs(suffix[k] - nums[k] * (len(prefix)-1 - k))

            output.append(left_sum + right_sum)
            
        return output
        