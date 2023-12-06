class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        out_put = []
        neg = []
        pos = []

        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        left=0
        while left < len(neg):
            out_put.append(pos[left])
            out_put.append(neg[left])
            left += 1

        return out_put

        