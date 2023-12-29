class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(array , k):
            left = array[:k + 1]
            right = array[k + 1:]

            left = left[::-1]
            output = left + right
    

            return output
        
        count = []


        for i in range(len(arr), 0 , -1):
            
            max_index  = arr.index(i)
            
            arr = flip(arr,max_index)
            arr = flip(arr, i - 1)

            count.append(max_index + 1)
            count.append(i)


        return count
           