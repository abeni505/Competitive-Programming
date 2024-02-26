class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rec(n):

            if n == len(s):
                return
                
            temp = s[n]
            rec(n+1)
            
            s[-1 - n] = temp
            # print(s[n])
            
        rec(0)
        

     