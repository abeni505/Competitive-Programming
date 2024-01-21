class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        
        prefix = [0] *(len(nums) + 1)
        max_ = 0
        for x , y in requests:
            prefix[x] += 1
            prefix[y + 1] -= 1
        prefix = list(accumulate(prefix))

        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        
        max_count = 0
        for i in range(len(nums)):
            max_count += (nums[i] * prefix[i])
            


        return max_count % (10**9 + 7)
