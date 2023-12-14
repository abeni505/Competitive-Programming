class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        max_ = 0

        for i in hashset:
            if i - 1 in hashset:
                continue
            
            else:
                conseq = 1
                while i + conseq in hashset:
                    conseq += 1

                max_ = max(max_,conseq)

        return max_

        
        
