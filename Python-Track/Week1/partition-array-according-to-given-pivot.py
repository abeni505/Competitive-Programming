class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        out_put = [0]*len(nums)

        less_max = 0
        equal_max = 0

        for i in nums:
            if i < pivot:
                less_max += 1
            elif i == pivot:
                equal_max += 1

        left = 0
        right = less_max + equal_max
        
        for i in nums:
            if i < pivot:
                out_put[left] = i
                left += 1
            elif i == pivot:
                out_put[less_max] = i
                less_max += 1
            else: 
                out_put[right] = i
                right += 1

        return out_put

            
        