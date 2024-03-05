class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        subsets = []
        curr = []

        def backtrack(indx):
            if indx == len(nums):
                subsets.append(curr[:])
                return

            curr.append(nums[indx])
            backtrack(indx + 1)
            curr.pop()

            backtrack(indx + 1)
        
        backtrack(0)
        

        summ = 0

        # print(subsets)
        for i in subsets:
          
            curr_xor = 0
            for ele in i:
                curr_xor ^= ele

            summ += curr_xor


        return summ
            