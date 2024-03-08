class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        max_ = max(count.values())
        ans = 0
        for value in count.values():
            if value == max_:
                ans += value

        return ans


