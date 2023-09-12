class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count =0
        new_nums=str(num)
        for i in range(len(new_nums)-k+1):
            window = new_nums[i:i+k]
            if int(window)!=0 :
                if num %int(window)==0:
                    count+=1
        return count
        
        