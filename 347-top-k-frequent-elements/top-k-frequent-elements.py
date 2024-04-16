class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        output = []
        for i in  count.most_common(k):
            output.append(i[0])
        
        return output
