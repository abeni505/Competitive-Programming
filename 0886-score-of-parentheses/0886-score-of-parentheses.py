class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        val=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(val)
                val=0
            else:
                val=stack.pop()+max(val*2,1)
        return val