class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        output = []
        count = Counter(arr1)
        for i in range(len(arr2)):
            for j in range(count[arr2[i]]):
                output.append(arr2[i])

        output2 = []
        for j in arr1:
            if j not in arr2:
                output2.append(j)
        output2.sort()
        
        return output + output2