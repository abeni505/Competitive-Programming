class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_element = nums[0]
        max_element = float('inf')

        for i in range(len(nums)):
            if nums[i] <= min_element:
                min_element = nums[i]

            elif nums[i] <= max_element:
                max_element = nums[i]

            else:
                return True
        return False
        
  


