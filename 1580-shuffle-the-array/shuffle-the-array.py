class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        out_put = []
        
        left = 0
        right = len(nums)//2

        while left < len(nums)//2 and right < len(nums):
            out_put.append(nums[left])
            out_put.append(nums[right])

            left += 1
            right += 1
            
        return out_put
        