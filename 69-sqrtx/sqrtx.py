class Solution:
    def mySqrt(self, x: int) -> int:
        
       
        
        left = 1
        right = x
        
    
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
            
        if x == 0:
            return 0
        return right 
            
        
                
        