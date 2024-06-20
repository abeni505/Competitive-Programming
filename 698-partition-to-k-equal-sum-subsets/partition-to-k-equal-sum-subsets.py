class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        reqSum = total // k
        subSets = [0] * k
        nums.sort(reverse = True)

        def recurse(i):
            if i == len(nums):    
                return True

            for j in range(k):
                if subSets[j] + nums[i] <= reqSum:
                    subSets[j] += nums[i]

                    if recurse(i + 1):
                        return True

                    subSets[j] -= nums[i]
                    if subSets[j] == 0:
                        break


            return False

        return recurse(0)