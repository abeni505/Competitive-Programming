class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        
        output = []
        

        # def backtrack(nums):
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            poped = nums.pop(0)
            
            path = self.permute(nums)
            for p in path:
                p.append(poped)
            
            output.extend(path)
            nums.append(poped)

        # backtrack(nums)
        return output
                