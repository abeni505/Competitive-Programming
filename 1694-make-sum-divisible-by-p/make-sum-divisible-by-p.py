class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = -1

        Total = sum(nums) % p
        if not Total:
            return 0 

        pre_right = 0
        count = len(nums)
        for i in range(len(nums)):
            pre_right += nums[i]

            pre_left = pre_right % p
            check = (pre_right % p - Total) % p
            
            if check in prefix:
                count = min(count , i - prefix[check])

            prefix[pre_left] = i

        return count if count < len(nums) else -1