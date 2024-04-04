class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        
        if target <= startValue:
            return startValue - target

        if target % 2:
            return self.brokenCalc(startValue,target + 1) + 1
        else:
            return self.brokenCalc(startValue,target // 2) + 1

        