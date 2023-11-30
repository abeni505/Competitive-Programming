class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr = []

        n = (num - 3)/3

        if n % 1 == 0:
            arr = [int(n),int(n+1),int(n+2)]
            
        return arr


