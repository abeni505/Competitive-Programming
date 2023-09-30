class Solution:
    def finalString(self, s: str) -> str:
        newstr=""
        for i in s:
            if i != "i":
                newstr+=i
            else:
                newstr=newstr[::-1]
            

        return newstr