class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nu=nums.sort()
        pt1=0
        pt2=-1
        while pt1+abs(pt2)<=len(nums):
            if nums[pt1]+nums[pt2]>target:
                pt2-=1
            elif nums[pt1]+nums[pt2]<target:
                pt1+=1
            else:
                return [pt1+1,len(nums)+pt2+1]
        




                


        



            