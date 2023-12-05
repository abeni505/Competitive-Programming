class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_ = ""
        for i in range(2,len(num)):
            if num[i-2]== num[i-1] == num[i]:
                cur_max = num[i-2]+num[i-1]+num[i]
                max_ = max(max_,cur_max)
        
        return max_

                 

        


        