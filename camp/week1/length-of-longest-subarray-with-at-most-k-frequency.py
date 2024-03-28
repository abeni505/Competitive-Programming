class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left = max_ = 0
        check = defaultdict(int)
        for right in range(len(nums)):
            check[nums[right]] += 1
 
            while check[nums[right]] > k:
                check[nums[left]] -= 1

                if check[nums[left]] == 0:
                    del check[nums[left]]

                left += 1
            
            max_ = max(max_ , right - left + 1)

        return max_