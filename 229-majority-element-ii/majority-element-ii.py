class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = len(nums)//3

        ans = []
        count = Counter(nums)

        for num in count.keys():
            if count[num] > target:
                ans.append(num)

        return ans