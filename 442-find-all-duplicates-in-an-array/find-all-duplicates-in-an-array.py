class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       
        output = []
        for i in range(len(nums)):
            while nums[i] != i + 1:

                temp = nums[i] - 1
                if nums[temp] == temp + 1:
                    output.append(temp + 1)
                    break

                nums[i], nums[temp] = nums[temp], nums[i]

        return set(output)