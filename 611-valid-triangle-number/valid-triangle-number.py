class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        total = 0


        for target in range(len(nums)-1,1,-1):

            right = target - 1
            left = 0

            while left < right:
                if nums[left] + nums[right] > nums[target]:
                    total += right - left
                    right -= 1

                else:
                    left += 1
        return total


