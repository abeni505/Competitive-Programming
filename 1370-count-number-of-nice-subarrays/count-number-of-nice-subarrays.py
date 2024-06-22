class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atmostK(k):
            left = 0
            window = set()
            odd_count = total_count = 0
            for right in range(len(nums)):
                window.add(nums[right])
                if nums[right] % 2:
                    odd_count += 1
                
                while odd_count > k:
                    if nums[left] % 2:
                        odd_count -= 1
                    left += 1

                total_count += right - left + 1

            return total_count
        
        return atmostK(k) - atmostK(k - 1)

