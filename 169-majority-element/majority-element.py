class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        operation = len(nums) // 2
        count = Counter(nums)
        for i in nums:
            if count[i] > operation:
                return i