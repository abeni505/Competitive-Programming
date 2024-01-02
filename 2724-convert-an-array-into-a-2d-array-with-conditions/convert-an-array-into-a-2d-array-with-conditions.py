class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        
        count = Counter(nums)

        max_ = max(count.values())
        output = [[] for _ in range(max_)]

        for key , value in count.items():
            for i in range(value):
                output[i].append(key)

        return output