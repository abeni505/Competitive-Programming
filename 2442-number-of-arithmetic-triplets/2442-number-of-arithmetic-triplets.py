class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        i=0
        j=1
        k=2
        n=len(nums)
        count=0
        while i<n and j <n and k<n:
            if nums[j]-nums[i]<diff:
                j+=1
            elif nums[j]-nums[i]>diff:
                i+=1
            else:
                if nums[k]-nums[j]<diff:
                    k+=1
                elif nums[k]-nums[j]>diff:
                    j+=1
                else:
                    count+=1
                    k+=1
                    
        return count
