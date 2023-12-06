class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
    
        less = []   
        equal = []
        greater = []

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        
        out_put = less + equal + greater
        return out_put
        