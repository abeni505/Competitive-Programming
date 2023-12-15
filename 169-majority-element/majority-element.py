class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        operation = len(nums) // 2
        count = Counter(nums)
        hashset = set(nums)
        
        for i in hashset:
            if count[i] > operation:
                return i