class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # check if it is left sorted portion of the array
            if nums[mid] >= nums[left] :

                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
                
        return -1

        