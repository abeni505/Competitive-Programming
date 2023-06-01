class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        slice1=nums[:n]
        slice2=nums[n:]
        arr=[]
        for i in range(n):
            arr.append(slice1[i])
            arr.append(slice2[i])

        return arr
