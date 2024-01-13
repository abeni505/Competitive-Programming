class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        left = count_odd = curr_good = 0
        n = len(nums)
        total = 0

        for right in range(n):
            

            if nums[right] % 2 != 0:
                count_odd += 1
                curr_good = 0

            while count_odd == k:

                curr_good += 1
                if nums[left] % 2 != 0:
                    count_odd -= 1
                    
                left += 1
            total += curr_good
                
        return total
