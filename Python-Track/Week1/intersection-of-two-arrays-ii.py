class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        s1 = set(nums1)
        s2 = set(nums2)

        output = []
        for i in s1:
            if i in s2:
                for _ in range(min(count1[i],count2[i])):
                    output.append(i)

        return output
