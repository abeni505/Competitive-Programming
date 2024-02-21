class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        total = 0


        for i in range(len(nums)-2):

            left = 0
            right = len(nums) - i - 2

            target = nums[len(nums) - i - 1]
            while left < right:
                if nums[left] + nums[right] > target:
                    total += right - left
                    right -= 1

                else:
                    left += 1
        return total


