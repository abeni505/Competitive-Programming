class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1

        curr_sum = count = 0
        for i in nums:
            curr_sum += i

            pre_right = curr_sum % k

            if pre_right in prefix:
                count += prefix[pre_right]

                prefix[pre_right] += 1
            
            else:
                prefix[pre_right] = 1

        return count


