class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(array , index):
            left = 0
            right = index 

            while left < right:
                array[left] , array[right] = array[right], array[left]
                left += 1
                right -= 1
        

        output = []
        for i in range(len(arr)-1,-1,-1):

            max_index = arr.index(i + 1)

            flip(arr, max_index)
            output.append(max_index + 1)

            flip(arr, i)
            output.append(i + 1)

        return output
