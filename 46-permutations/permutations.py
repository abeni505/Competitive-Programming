class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            poped = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(poped)
            
            output.extend(perms)
            nums.append(poped)

        return output