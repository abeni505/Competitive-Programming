class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        return count.most_common(1)[0][0]


