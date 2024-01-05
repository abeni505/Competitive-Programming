class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        greater = [1] * len(nums)

        for holder in range(len(nums)-1,-1,-1):
            for seeker in range(holder + 1,len(nums)):

                if nums[holder] < nums[seeker]:
                    greater[holder] = max(greater[holder], 1 + greater[seeker])
                    
            # print(greater)
        return max(greater)