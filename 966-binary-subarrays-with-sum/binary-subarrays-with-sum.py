class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        
        curr_sum = count = 0

        hashmap = defaultdict(int)
        hashmap[0] = 1

        for i in nums:
            curr_sum += i
      
            count += hashmap[curr_sum - goal]
            hashmap[curr_sum] += 1

        return count

            
