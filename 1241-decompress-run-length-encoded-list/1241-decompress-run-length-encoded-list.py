class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr=[]
        i=0
        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]

            for j in range(freq):
                arr.append(val)
    
        return arr