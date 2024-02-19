class Solution:
    def minimumSteps(self, s: str) -> int:
    
        count = 0
        step = 0

        for i in s:
            if i == "1":
                count += 1
            else:
                step += count

        return step