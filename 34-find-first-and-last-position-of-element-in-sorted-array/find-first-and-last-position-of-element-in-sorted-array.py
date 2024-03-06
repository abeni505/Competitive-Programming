class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = -1
        right = len(nums) - 1

        if len(nums) == 0:return [-1,-1]

        output = []
        while left + 1 < right:
            mid = (left + right)//2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if nums[right] == target:
            output.append(right)
        else:
            output.append(-1)

        left2 = 0
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid 

        if nums[left] == target:
            output.append(left)
        else:
            output.append(-1)

        return output