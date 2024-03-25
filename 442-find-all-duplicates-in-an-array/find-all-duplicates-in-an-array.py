class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        output = []
        for key , val in count.items():
            if val > 1:
                output.append(key)

        return output
