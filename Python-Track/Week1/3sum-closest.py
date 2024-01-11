class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_ = float('inf')

        min_sum = 0
        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(target - cur_sum ) < min_:
                    min_ = abs(target - cur_sum)
                    min_sum = cur_sum
                
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return target

        return min_sum
                