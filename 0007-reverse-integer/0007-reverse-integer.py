class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            x=abs(x)
            flag=True
        x_rev=str(x)[::-1]
        if flag:
            output=int("-"+x_rev)
        else:
            output=int(x_rev)
        if (-2**31)<= output<=((2**31)-1):
            return output
        else:
            return 0

            
        