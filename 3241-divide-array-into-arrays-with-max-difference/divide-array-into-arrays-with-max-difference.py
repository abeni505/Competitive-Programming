class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
   
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(0, n, 3):
            a, b, c = nums[i:i+3]

            if c - a <= k:
                ans.append([a, b, c])
            else:
                ans.clear()
                return ans
        return ans



