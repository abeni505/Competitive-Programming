class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new_nums = []

        for i in range(0,len(nums)-1,2):
            freq , val = nums [i],nums[i+1]

            for j in range(freq):

                new_nums.append(val) 

        return new_nums