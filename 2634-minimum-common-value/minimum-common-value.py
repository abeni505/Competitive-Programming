class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1.sort()
        nums2.sort()

        left = right = 0


        while left < len(nums1) and right < len(nums2): 

            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                return nums1[left]

        return -1