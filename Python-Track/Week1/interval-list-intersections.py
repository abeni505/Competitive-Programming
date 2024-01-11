class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []

        left = right = 0

        while left < len(firstList) and right < len(secondList):
            x = max(firstList[left][0] , secondList[right][0])
            y = min(firstList[left][1] , secondList[right][1])

            if x <= y:
                output.append([x,y])
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1

        return output