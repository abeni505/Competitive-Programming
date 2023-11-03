class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        left=0
        count={}
        max_length=float("-inf")

        for right in range(len(answerKey)):

            count[answerKey[right]] = 1 + count.get(answerKey[right],0)
            if (right - left + 1) - max(count.values()) > k:
                count[answerKey[left]] -= 1
                left+=1

            max_length=max(max_length,right - left + 1)
        
        return max_length
