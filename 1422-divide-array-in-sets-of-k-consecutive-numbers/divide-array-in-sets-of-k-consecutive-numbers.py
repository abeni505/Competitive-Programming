class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        
        sorted_keys = sorted(count.keys())

        for key in sorted_keys:
            if count[key] > 0:
                for i in range(1, k):
                    if count[key + i] < count[key]:
                        return False
                    count[key + i] -= count[key]
        return True
        