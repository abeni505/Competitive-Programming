class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = -1
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right)//2

            if nums[mid] >= target:
                right = mid 
            else:
                left = mid 

        if nums[right] == target:
            return right
        else:
            return -1