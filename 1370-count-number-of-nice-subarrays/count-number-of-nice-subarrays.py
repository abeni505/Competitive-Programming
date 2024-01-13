class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            left = count_odd = 0
            n = len(nums)
            total = 0

            for right in range(n):
                

                if nums[right] & 1:
                    count_odd += 1
            
                while count_odd > k:
                    if nums[left] & 1:
                       count_odd -= 1

                    left += 1
                total += right - left + 1
                
            return total
                
        return atmost(k) - atmost(k - 1)
