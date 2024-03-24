class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        solved = set()

        for i in range(len(nums)):
            while nums[i] != i + 1:

                if nums[i] in solved:
                    return nums[i]

                solved.add(nums[i])
                
                temp = nums[i]
                nums[i], nums[temp - 1] = nums[temp - 1], nums[i]





