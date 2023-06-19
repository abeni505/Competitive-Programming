class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left=0
        length=len(arr)
        while left<length:
            if arr[left]==0:
                arr.insert(left+1,0)
                left+=1
            left+=1

        arr[:]=arr[:length]
        