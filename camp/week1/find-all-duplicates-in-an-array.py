class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        output = []
        for i in range(len(nums)):

            while nums[i] != i + 1 and nums[i] != -1:
                temp = nums[i] - 1

                if nums[i] in visited:
                    output.append(nums[i])
                    nums[i] = - 1
                    continue
                visited.add(nums[i])
                
                nums[i] , nums[temp] = nums[temp] , nums[i]

        return output