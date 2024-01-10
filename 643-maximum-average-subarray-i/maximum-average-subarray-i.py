class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left = right = 0
     
        max_avg = float('-inf')
        cur_sum = 0
        
        while right < len(nums):
            if right - left  <= k:
                cur_sum += nums[right]
                right += 1
                
                if right - left == k:
                    max_avg = max(max_avg,cur_sum/k)
                    cur_sum -= nums[left]
                    left += 1
   
        return max_avg

