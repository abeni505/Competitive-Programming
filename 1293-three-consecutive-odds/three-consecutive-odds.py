class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            if arr[i] % 2:
                arr[i] = 1
            else:
                arr[i] = 0
        
        window = sum(arr[0:3])

        if window == 3:
            return True
        
        for indx in range(3,len(arr)):
            window += arr[indx]
            window -= arr[indx - 3]

            if window == 3:
                return True

        return False