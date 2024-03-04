class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(start ,subset):

            output.append(subset[:])

            for i in range(start , len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)

                subset.pop()


        backtrack(0,[])
        return output