class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        a = nums1[0]
        b = nums2[0]
        visited = set()
        heap = [(a + b ,0, 0)]
        visited.add((0,0))

        output = []

        while heap and len(output) < k:

            summ ,left , right = heappop(heap)
            output.append((nums1[left] , nums2[right]))

            if left < len(nums1) - 1 and (left + 1,right) not in visited:
                a , b = nums1[left + 1] , nums2[right] 
                heappush(heap , (a + b, left + 1, right))
                visited.add((left + 1 , right))

        
            if right < len(nums2) - 1 and (left, right + 1) not in visited:
                a , b = nums1[left] , nums2[right + 1] 
                heappush(heap , (a + b, left, right + 1))
                visited.add((left, right + 1))

        return output