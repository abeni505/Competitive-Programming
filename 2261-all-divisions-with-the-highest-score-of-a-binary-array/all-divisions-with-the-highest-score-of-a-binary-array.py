class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        m_score = { 0 : sum(nums), len(nums):len(nums) - sum(nums) }
        score = sum(nums)
       
        
        total_sum = 0
        for i in range(0,len(nums)-1):
            cur_score = 0
            total_sum += nums[i]
            nums_left = (i+1) - total_sum
            nums_right = score - total_sum

            cur_score = nums_left + nums_right
            m_score[i+1] = cur_score


        max_val = 0
        for key, val in m_score.items():
            if val > max_val:
                max_val = val

        output = []
        for key, val in m_score.items():
            if val == max_val:
                output.append(key)
        
        return output
            # score = nums_left + nums_right
            # max_score = max(max_score,score)
            # m_score[score] = i
