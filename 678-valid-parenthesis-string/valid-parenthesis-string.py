class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        extra = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    if extra:
                        extra.pop()
                    else:
                        return False
            else:
                extra.append(i)

        if not stack:
            return True
        
        print(stack,extra)
        while stack and extra:
            if stack.pop() > extra.pop():
                return False

        return not stack

