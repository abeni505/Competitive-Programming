class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        arr=[]
        for i in candies:
            if i+extraCandies>= max(candies):
                bool=True
                arr.append(bool)
            else:
                bool=False
                arr.append(bool)

        return arr