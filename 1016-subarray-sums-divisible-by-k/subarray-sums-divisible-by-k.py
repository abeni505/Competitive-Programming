class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1

        pre_right = count = 0
        for num in nums:
            pre_right += num
            # PL % k = PR % k 
            pre_left = pre_right % k
            count += prefix[pre_left]

            prefix[pre_right % k] += 1

        return count


