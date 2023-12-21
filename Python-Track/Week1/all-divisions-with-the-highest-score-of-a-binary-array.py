class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        score = sum(nums)

        m_score = defaultdict(list) 
        m_score[score].append(0)
        m_score[ len(nums) - score].append(len(nums))

        
        total_sum = 0
        for i in range(len(nums)-1):
            cur_score = 0
            total_sum += nums[i]
            nums_left = (i+1) - total_sum
            nums_right = score - total_sum

            cur_score = nums_left + nums_right
            m_score[cur_score].append(i+1) 


        max_val = max(m_score.keys())

    
        return m_score[max_val]
            # score = nums_left + nums_right
            # max_score = max(max_score,score)
            # m_score[score] = i
