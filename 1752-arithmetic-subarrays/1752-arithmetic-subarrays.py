class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(subarray):
            subarray.sort()
            diff = subarray[1] - subarray[0]
            for i in range(2, len(subarray)):
                if subarray[i] - subarray[i - 1] != diff:
                    return False
            return True

        results = []
        for left, right in zip(l, r):
            subarray = nums[left:right + 1]
            if is_arithmetic(subarray):
                results.append(True)
            else:
                results.append(False)
        
        return results
