class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []

        hashmap = {}

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                hashmap[stack.pop()] = nums2[i]

            stack.append(nums2[i])

        output = []
        for num in nums1:
            output.append(hashmap.get(num , -1))
            
        return output
