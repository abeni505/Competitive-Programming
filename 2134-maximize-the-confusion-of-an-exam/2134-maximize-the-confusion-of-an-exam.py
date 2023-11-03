class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        left=0
        count={"T":0,"F":0}
        max_length=float("-inf")

        for right in range(len(answerKey)):

            count[answerKey[right]] +=1
            if min(count.values()) > k:
                count[answerKey[left]] -= 1
                left+=1

            max_length=max(max_length,right - left + 1)
        
        return max_length
