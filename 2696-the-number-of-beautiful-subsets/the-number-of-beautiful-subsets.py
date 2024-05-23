class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        count = 0
        subset = []
        def backtrack(start):
            nonlocal count
            count += 1
            
            for i in range(start, len(nums)):
                num = nums[i]
                
                if num + k not in subset and num - k not in subset:
                    subset.append(num)
                    backtrack(i + 1)
                    subset.pop()
        
        backtrack(0)
        return count - 1