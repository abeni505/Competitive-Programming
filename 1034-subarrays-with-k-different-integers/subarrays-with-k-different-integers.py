class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        left = left2 = count = count2 = 0
        window = defaultdict(int)
        window2 = defaultdict(int)

        for right in range(len(nums)):

            window[nums[right]] += 1
            while len(window) > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1

            count += right - left + 1
            
            window2[nums[right]] += 1
            while len(window2) > k - 1:
                window2[nums[left2]] -= 1
                if window2[nums[left2]] == 0:
                    del window2[nums[left2]]
                left2 += 1

            count2 += right - left2 + 1
        
        return count - count2
