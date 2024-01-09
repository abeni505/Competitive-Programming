class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        hashset = set()

        for right in range(len(nums)):
            if right > left + k :
                hashset.remove(nums[left])
                left += 1
                
            if nums[right] in hashset:
                return True
            hashset.add(nums[right])

        return False
            


