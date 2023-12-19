class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        array = [ i for i in range(1 , n+1)]

        # for i in range(ceil(n/2)):
        #     if i % k == 0:
        #         array.pop(array[i])
        nums = [0] * n
        count = 0
        i = 0
        while count < n - 1:
            r = k
            
            while r > 0:
                i = (i + 1) % n  
                if nums[i] == 0:
                    r -= 1

            nums[i] = 1
            count += 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return array[i-1]