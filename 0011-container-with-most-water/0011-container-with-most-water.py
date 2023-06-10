class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        cur_max=0
        
        while left<=right:
            width=right-left
            h=min(height[left],height[right])
            area=width*h
            cur_max=max(cur_max,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return cur_max


        