class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stackb=[]
        new_s=""
        new_t=""

        for i in s:
            if i=="#":
                stack and stack.pop()

            else:
                stack.append(i)

        for j in t:
            if j=="#":
                stackb and stackb.pop()
            else:
                stackb.append(j)

        for k in stack:
            new_s+=k
        for l in stackb:
            new_t+=l

        return new_s==new_t