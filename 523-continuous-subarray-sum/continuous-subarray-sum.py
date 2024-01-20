class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = defaultdict(int)
        prefix[0] = -1
        
        pre_sum = 0
        for i in range(len(nums)):

            pre_sum  += nums[i] 
            pre_right = pre_sum % k
            print(pre_right)

            if pre_right in prefix:
                if i - prefix[pre_right] > 1:
                    return True
            else:
                prefix[pre_right] = i

        return False
                