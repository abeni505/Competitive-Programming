class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right=len(nums)-1
        inserted=0
        while inserted<k:
            nums.insert(0,nums[right])
            nums.pop()
            inserted+=1
        

        return nums