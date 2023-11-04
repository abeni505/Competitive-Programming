class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        output=[0]*len(nums)

        prefix=0
        for i in range(len(nums)):
            output[i]=prefix
            prefix+=nums[i]
        postfix=0
        for j in range(len(nums)-1,-1,-1):
            output[j] = abs(output[j]-postfix)
            postfix+=nums[j]

        return output
        