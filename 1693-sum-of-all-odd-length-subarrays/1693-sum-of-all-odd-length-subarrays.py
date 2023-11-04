class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        total_sum = 0

        for left in range(len(arr)):

            cur_sum = 0
            for right in range(left,len(arr)):
                cur_sum += arr[right]
                if (right - left + 1) % 2 != 0:
                    total_sum += cur_sum  

                
        return total_sum