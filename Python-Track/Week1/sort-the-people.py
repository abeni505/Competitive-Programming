class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        swapped = False
        for i in range(len(names)):
            for j in range(len(names) - 1 - i):
                if heights[j] < heights[j+1]:
                    heights[j] , heights[j+1] = heights[j+1] , heights[j]
                    names[j] , names[j+1] = names[j+1] , names[j]
                    swapped = True

            if not swapped :
                break
                               
        return names

