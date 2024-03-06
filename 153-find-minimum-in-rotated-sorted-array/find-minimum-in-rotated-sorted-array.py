class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = -1
        right = len(nums) - 1

        while left + 1 < right:
    
            mid = (left + right)//2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        
        # print(right)
        return nums[right]
