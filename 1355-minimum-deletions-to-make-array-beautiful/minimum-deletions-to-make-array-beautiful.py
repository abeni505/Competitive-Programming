class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i = 0
        delcnt=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                delcnt+=1
                i+=1
            else:
                i+=2
        if (len(nums)- delcnt) % 2:
            delcnt += 1
        return delcnt