class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index

        for oldvalue, newvalue in operations:
            if oldvalue in hashmap:
                index = hashmap[oldvalue]
                nums[index] = newvalue
                hashmap[newvalue] = index

        return nums

        
        