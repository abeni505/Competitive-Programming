class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def subarrayatmostk(k):

            window = defaultdict(int)

            count = left = 0
            for right in range(len(nums)):

                window[nums[right]] += 1
                while len(window) > k:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                    left += 1

                count += right - left + 1
            
            return count
        
        return subarrayatmostk(k) - subarrayatmostk(k - 1)
