class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            
            curr += num
            ans += counts[curr - goal]
            counts[curr] += 1

        return ans
