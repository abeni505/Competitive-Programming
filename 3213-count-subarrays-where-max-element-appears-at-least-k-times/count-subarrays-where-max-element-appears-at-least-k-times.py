class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        

        max_ele = max(nums)

        count = defaultdict(int)

        left = output = 0
        for right in range(len(nums)):

            count[nums[right]] += 1

            while count[max_ele] >= k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]] 

                left += 1

            output += left

        return output
            