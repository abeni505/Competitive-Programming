class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        left = max_ = 0

        count = defaultdict(int)
        count["T"] = 0
        count["F"] = 0

        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            
            while min(count.values()) > k:
                count[answerKey[left]] -= 1
                left += 1

            max_ = max(max_ , right - left + 1)

        return max_


            