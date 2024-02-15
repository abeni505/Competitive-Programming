class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums),2, -1):
            print(i,nums[:i - 1],nums[i - 1])
            if sum(nums[:i - 1])>nums[i - 1]:
                return sum(nums[:i])
        return -1