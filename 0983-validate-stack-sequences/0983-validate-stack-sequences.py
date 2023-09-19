class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        ptr=0
        stack=[]

        for i in pushed:
            stack.append(i)
            
            while ptr<len(popped) and stack and popped[ptr]==stack[-1]:
                stack.pop()
                ptr+=1

        return not stack