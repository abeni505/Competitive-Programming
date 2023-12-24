class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        
        peak_index = 0
        for i in range(1,len(arr) - 1):
            if arr[i -1] >= arr[i] <= arr[i + 1]:
                return False
        
        count = 0
        for i in range(1,len(arr) - 1):
            if arr[i -1] < arr[i] > arr[i + 1]:
                peak_index = i
                count += 1
       
        
        for j in range(0,peak_index):
            if arr[j] >= arr[peak_index]:
                return False

        for k in range(peak_index + 1 ,len(arr)):
            if arr[k] >= arr[peak_index]:
                return False

        if count == 1:
            return True
        else:
            return False