class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = len(nums)//3

        ans = []
        count = Counter(nums)

        for i in count.keys():
            if count[i] > target:
                ans.append(i)

        return ans