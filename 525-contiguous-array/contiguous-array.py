class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = -1

        pre_sum = max_len = 0
        for i in range(len(nums)):
            
            if nums[i]:
                pre_sum += 1
            else:
                pre_sum -= 1

            if pre_sum in prefix:
                max_len = max(max_len , i - prefix[pre_sum])
            else:
                prefix[pre_sum] = i

        return max_len
                
