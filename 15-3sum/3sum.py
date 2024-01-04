class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twosum(nums,target):
            left = 0
            right = len(nums) - 1

            output = []
            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1

            return output
        nums.sort()

        left = 0
        hashset = set()
        while left < len(nums) - 1:
            target = 0 - nums[left]

            check = twosum(nums[left + 1:], target)

            for i in range(len(check)):
                x = [nums[left]]+ check[i]
                hashset.add(tuple(x))
                  
            left += 1
            

        return list(hashset)
        