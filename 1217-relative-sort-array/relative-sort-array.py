class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        output = []
        for i in arr2:
            j = count[i]
            for _ in range(j):
                output.append(i)
                count[i] -= 1

        count = dict(sorted(count.items() , key = lambda x: x[0]))

        for key , value in count.items():
            if count[key]:
                for _ in range(value):
                    output.append(key)
              
        return output 
