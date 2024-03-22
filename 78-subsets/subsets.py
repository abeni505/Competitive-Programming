class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(index , currans):
            if index == len(nums):
                ans.append(currans.copy())
                return

            currans.append(nums[index])
            backtrack(index + 1 , currans)

            currans.pop()
            backtrack(index + 1 , currans)

        backtrack(0 , [])
        return ans