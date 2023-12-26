class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hashmap = dict()
        for i in range(len(names)):
            hashmap[heights[i]] = names[i]

        for i in range(len(names)):
            for j in range(len(names) - 1 - i):
                if heights[j] < heights[j+1]:
                    heights[j] , heights[j+1] = heights[j+1] , heights[j]

        output = []
        for i in heights:
            output.append(hashmap[i])

        return output


