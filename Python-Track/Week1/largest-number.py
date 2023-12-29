class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(s1,s2):
            s1 = str(s1)
            s2 = str(s2)

            if int(s1 + s2) > int(s2 + s1):
                return True
            return False

        for i in range(len(nums)): # bubble sort 
            for j in range(len(nums) - 1 - i):
                if not compare(nums[j] , nums[j + 1]):
                    nums[j] , nums[j + 1] = nums[j + 1] , nums[j]

        ans = list(map(str,nums))
        ans = "".join(ans)

        return str(int(ans))
