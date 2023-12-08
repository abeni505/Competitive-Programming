class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        checker = {i for i in range(left , right + 1)}
        elements = set()

        for min_ , max_ in ranges:

            elements.update(range(min_ , max_ + 1))

        if checker <= elements:
            return True
            
        return False
        

        