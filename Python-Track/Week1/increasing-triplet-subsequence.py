class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        max_ = []
        min_ = []

        min_element = float('inf')
        max_element = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            cur_max = nums[i]
            max_.append(max(max_element,cur_max))
            max_element = max_[-1]
        max_ = max_[::-1]

        for j in range(len(nums)):
            cur_min = nums[j]
            min_.append(min(min_element,cur_min))
            min_element = min_[-1]

        # print(max_)
        # print(min_)
  
        for k in range(len(nums)):
            if nums[k] > min_[k] and nums[k] < max_[k]:
                return True

        return False