class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_sub=0

        for i in range(len(s)):
            count=1
            for j in range(i+1,len(s)):
                if s[j] not in  s[i:j]:
                    count+=1
                else:
                    break
            longest_sub=max(longest_sub,count)

        return longest_sub

            
                    
        
