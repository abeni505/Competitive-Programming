class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)

        for i in range(n):
            check = n - bisect_left(nums,i + 1)
            if check == i + 1:
                return check

        return -1

