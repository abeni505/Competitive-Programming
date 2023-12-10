class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        print(hashmap)

        for old , new in operations:
            if old in hashmap:
              
                nums[hashmap[old]] = new
                hashmap[new] = hashmap.pop(old) # removes old from hashmap and assigns its value to new            
                
        return nums

