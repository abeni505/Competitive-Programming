class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = seeker = 0
        right = len(nums) - 1
        

        while seeker <= right:
            
            if nums[seeker] == 0:
                nums[left], nums[seeker] = nums[seeker] , nums[left]
                left += 1
                seeker += 1
                
            elif nums[seeker] == 2:
                nums[seeker] , nums[right] = nums[right] , nums[seeker]
                right -= 1
            else:
                seeker += 1
            


        
    