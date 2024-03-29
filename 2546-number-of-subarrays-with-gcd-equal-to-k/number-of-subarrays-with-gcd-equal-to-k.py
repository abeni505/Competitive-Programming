class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        count = 0
        for i in range(len(nums)):
            
            ans = nums[i]
            for j in range(i  ,len(nums)):
                ans = gcd(ans,nums[j])
                if ans == k:
                    count += 1

        return count