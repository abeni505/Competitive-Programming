class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        count_sort = [0] * (max(nums) + 1)

        for i in nums:
            count_sort[i] += 1

        new_nums = []
        pair = {0:0}
        run_sum = 0
        for j in range(1,len(count_sort)):
            run_sum +=  count_sort[j-1]

            pair[j] = run_sum

        for k in nums:
            new_nums.append(pair[k])
        # return pair
        return new_nums


