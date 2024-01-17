class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] 
        suffix = [1] 

        
        for i in range(len(nums)):
            prefix.append(prefix[-1] * nums[i])
        
        for j in range(len(nums)-1,-1,-1):
            suffix.append(suffix[-1] * nums[j])


        output = []
        suffix = suffix[::-1]

        for k in range(1 , len(suffix)):
            output.append(suffix[k] * prefix[k - 1])
            
        return output
