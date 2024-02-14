class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        output = []
        for i in range(len(pos)):
            output.append(pos[i])
            output.append(neg[i])

        return output