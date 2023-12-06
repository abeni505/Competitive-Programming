class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        out_put = [0]*len(nums)


        pos = 0
        neg = 1
        for i in nums:
            if i < 0:
                out_put[neg] = i
                neg += 2
            else:
                out_put[pos] = i
                pos += 2

        return out_put

        