class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr=[]
        for i in nums1:
            left=nums2.index(i)
            right=left+1
            appended=False
            while right<len(nums2) :
                if nums2[left]<nums2[right]:
                    arr.append(nums2[right])
                    appended=True
                    break
                else:
                    right+=1
            if not appended:
                arr.append(-1)
        
        return arr