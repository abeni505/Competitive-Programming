class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        for i in range(n):

            while nums[i] != i + 1:

                temp = nums[i] - 1

                if nums[i] == nums[temp]:
                    break

                nums[i] , nums[temp] = nums[temp] , nums[i]

        output = []
        for j in range(n):
            if nums[j] != j + 1:
                output.append(j + 1)

        return output

        # 1 2 3 4 3 2 7 8