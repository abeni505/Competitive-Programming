class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = defaultdict(int)
        prefix[0] = -1

        curr_sum = 0
        for i in range(len(nums)):

            curr_sum += nums[i]
            pre_right = curr_sum % k

            if pre_right in prefix:
                if i - prefix[pre_right] >= 2:
                    return True
      
            else:
                prefix[pre_right] = i
        
        
        return False