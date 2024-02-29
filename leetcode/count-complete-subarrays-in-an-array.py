class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
    
        check = len(set(nums))

        left = total = curr = 0
     
        hashmap = defaultdict(int)
        for right in range(len(nums)):
            
            hashmap[nums[right]] += 1

            while len(hashmap) == check:
                hashmap[nums[left]] -= 1
                
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1

                curr += 1

            total += curr

        return total