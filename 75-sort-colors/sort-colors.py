class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            curr_min = i
            for j in range(i + 1 , len(nums)):
                if nums[j] < nums[curr_min]:
                    curr_min = j
            
            nums[i] , nums[curr_min] = nums[curr_min] , nums[i]
        
        

        