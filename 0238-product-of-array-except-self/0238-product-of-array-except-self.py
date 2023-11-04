class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        Prefix = [1]* len(nums)
        Postfix = [1]* len(nums)
        output = []

        for i in range(1,len(nums)):
            Prefix[i] = Prefix[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            Postfix[j] = Postfix[j+1] * nums[j+1]

        for k in range(len(Prefix)):
            output.append(Prefix[k]*Postfix[k])

        return output
        

