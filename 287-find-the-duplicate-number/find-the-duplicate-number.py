class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        new = 0
        while new != slow:
            new = nums[new]
            slow = nums[slow]
        
        return new


