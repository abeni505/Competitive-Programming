class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    
        ptr1 = 0
        ptr2 = 0
        

        while ptr1 < m and ptr2 < n:
            if nums1[ptr1] <= nums2[ptr2]:
                ptr1 += 1
            else:
                nums1.insert(ptr1, nums2[ptr2])
                nums1.pop()
                m+=1
                ptr2 += 1

        if ptr2 < n:
            nums1[ptr1:] = nums2[ptr2:]

        # return nums1

