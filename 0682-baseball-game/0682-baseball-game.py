class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        stack_sum=0
        for i in operations:
            if i =="+":
                sum=stack[-1]+stack[-2]
                stack.append(sum)

            elif i =="D":
                double=stack[-1]*2
                stack.append(double)
            elif i =="C":
                stack.pop()
            else:
                stack.append(int(i))
        for i in stack:
            stack_sum+=i
        return stack_sum