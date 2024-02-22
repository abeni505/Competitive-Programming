class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        hashmap = {}
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                hashmap[stack.pop()] = i

            stack.append(i)

        output = []
        for i in range(len(temperatures)):
            output.append(hashmap.get(i, i) - i)

        return output