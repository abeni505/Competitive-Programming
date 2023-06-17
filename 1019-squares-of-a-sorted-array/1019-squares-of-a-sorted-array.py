class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left=0
        right=len(nums)-1
        arr=[]
        while left<=right:           
            if abs(nums[right])>abs(nums[left]):
                arr.append(nums[right]**2)
                right-=1
            else:
                arr.append(nums[left]**2)
                left+=1
        
        return arr[::-1]
                
            


