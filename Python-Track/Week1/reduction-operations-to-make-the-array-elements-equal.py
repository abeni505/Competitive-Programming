class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()

        output = 0
        cur = 0
        for i in range(len(nums)- 1):
            if nums[i] <  nums[i + 1]:
                cur += 1

            output += cur

        return output
        # x = len(set(nums)) - 1
        # arthi = x*(x + 1) // 2
        # return arthi
        

