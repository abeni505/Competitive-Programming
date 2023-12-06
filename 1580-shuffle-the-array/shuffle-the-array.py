class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        out_put = []
        left = nums[:(len(nums)//2)+1]
        right = nums[len(nums)//2:]

        for i in range(len(right)):
            out_put.append(left[i])
            out_put.append(right[i])

        return out_put

        