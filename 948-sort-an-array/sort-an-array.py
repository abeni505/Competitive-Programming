class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_ele = abs(min(nums))
        max_ele = max(nums) + min_ele
        counter = [0]*(max_ele +1)

        for i in nums:
            counter[i + min_ele] += 1
            
        output = []
    
        for j in range(len(counter)):
            for k in range(counter[j]):
                output.append(j - min_ele )

        return output
