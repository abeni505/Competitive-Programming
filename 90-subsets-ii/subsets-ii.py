class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        def backtrack(index , currans):
            if index == len(nums):

                ans.add(tuple(sorted(currans)))
                return

            if tuple(sorted(currans)) not in ans:

                currans.append(nums[index])
                backtrack(index + 1 , currans)

                currans.pop()
                backtrack(index + 1, currans)

        backtrack(0 , [])

        return ans
        