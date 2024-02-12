class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = Counter(nums)

        for key , val in count.items():
            if val > n//2:
                return key
